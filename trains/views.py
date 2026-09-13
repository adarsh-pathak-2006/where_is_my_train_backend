from django.shortcuts import get_object_or_404
from .models import Train, TrainStation
from .serializers import TrainSerializer, TrainStationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from wimt.cache_key import train_list_cache_key, train_all_station_cache_key
from wimt.pagination import GeneralPagination
from station.models import Station
from django.db.models import Q
from rest_framework.permissions import AllowAny

class AllTrainAPI(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        page_no=request.query_params.get("page", "1")
        cached_data=cache.get(train_list_cache_key(pageno=page_no))
        if cached_data:
            return Response(cached_data, status=200)
        paginator=GeneralPagination()
        queryset=paginator.paginate_queryset(Train.objects.select_related('starting_station', 'ending_station').all(), request, view=self)
        serial=TrainSerializer(queryset, many=True)
        response=paginator.get_paginated_response(serial.data)
        cache.set(train_list_cache_key(pageno=page_no), response.data, timeout=6000)
        return Response(response.data)

class TrainStationAPI(APIView):
    permission_classes=[AllowAny]
    def get(self, request, pk):
        cached_data=cache.get(train_all_station_cache_key(train_id=pk))
        if cached_data:
            return Response(cached_data, status=200)
        data=TrainStation.objects.select_related('train').filter(train__id=pk)
        serial=TrainStationSerializer(data, many=True)
        cache.set(train_all_station_cache_key(train_id=pk), serial.data, timeout=6000)
        return Response(serial.data, status=200)

class TrainEnquiryBasedOnStationAPI(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        from_station=request.query_params.get("from")
        to_station=request.query_params.get("to")
        from_station_data=get_object_or_404(Station, name=from_station)
        to_station_data=get_object_or_404(Station, name=to_station)

        # Get all TrainStation mappings for these two stations
        ts_from = TrainStation.objects.filter(station=from_station_data)
        ts_to = TrainStation.objects.filter(station=to_station_data)

        # Map train_id -> sequence for the "to" stations to allow fast lookup
        to_sequences = {ts.train_id: ts.sequence for ts in ts_to}

        valid_train_ids = []
        for ts in ts_from:
            to_seq = to_sequences.get(ts.train_id)
            if to_seq is not None and ts.sequence < to_seq:
                valid_train_ids.append(ts.train_id)

        valid_trains = Train.objects.select_related('starting_station', 'ending_station').filter(id__in=valid_train_ids)
        serial = TrainSerializer(valid_trains, many=True)
        return Response(serial.data, status=200)