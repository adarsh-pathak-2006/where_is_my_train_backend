from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Station
from .serializers import StationSerializer, TrainOnStationSerializer
from rest_framework.response import Response
from wimt.pagination import GeneralPagination
from django.core.cache import cache
from wimt.cache_key import station_cache_key
from rest_framework.permissions import AllowAny, IsAdminUser

class StationAPI(APIView):
    def get_permissions(self):
        if self.request.method=='GET':
            return [AllowAny()]
        return [IsAdminUser()]
    def get(self, request):
        page_no=request.query_params.get("page", "1")
        cached_data=cache.get(station_cache_key(pageno=page_no))
        if cached_data:
            return Response(cached_data, status=200)
        paginator=GeneralPagination()
        queryset=paginator.paginate_queryset(Station.objects.all(), request, view=self)
        serial=StationSerializer(queryset, many=True)
        response=paginator.get_paginated_response(serial.data)
        cache.set(station_cache_key(pageno=page_no), response.data, timeout=60000)
        return response

    def post(self, request):
        serial=StationSerializer(request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)    


class TrainOnStationAPI(APIView):
    def get(self, request, pk):
        data=get_object_or_404(Station, id=pk)
        serial=TrainOnStationSerializer(data)
        return Response(serial.data, status=200)