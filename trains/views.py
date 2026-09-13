from django.shortcuts import get_object_or_404
from .models import Train, TrainStation
from .serializers import TrainSerializer, TrainStationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from wimt.cache_key import train_list_cache_key, train_all_station_cache_key
from wimt.pagination import GeneralPagination

class AllTrain(APIView):
    def get(self, request):
        page_no=request.query_param.get("page", "1")
        cached_data=cache.get(train_list_cache_key(pageno=page_no))
        if cached_data:
            return Response(cached_data, status=200)
        paginator=GeneralPagination()
        queryset=paginator.paginate_queryset(Train.objects.select_related('trains_starting', 'trains_ending').all(), request, view=self)
        serial=TrainSerializer(queryset, many=True)
        response=paginator.get_paginated_response(serial.data)
        cache.set(train_list_cache_key(pageno=page_no), response.data, timeout=6000)
        return Response(response.data)

class TrainStationAPI(APIView):
    def get(self, request, pk):
        cached_data=cache.get(train_all_station_cache_key(train_id=pk))
        if cached_data:
            return Response(cached_data, status=200)
        data=TrainStation.objects.select_related('train__id').filter(train__id=pk)
        serial=TrainStationSerializer(data, many=True)
        cache.set(train_all_station_cache_key(train_id=pk), serial.data, timeout=6000)
        return Response(serial.data, status=200)
