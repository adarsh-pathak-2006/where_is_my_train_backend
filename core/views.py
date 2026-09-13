from django.shortcuts import get_object_or_404
from .models import CurrentStatus
from .serializers import CurrentStationGetSerializer, CurrentStationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser

class CurrentStatusAPI(APIView):
    def get_permissions(self):
        if self.request.method=='GET':
            return [AllowAny()]
        return [IsAdminUser()]
    def get(self, request, name):
        data=get_object_or_404(CurrentStatus.objects.select_related('train', 'previous_station', 'upcoming_station', 'nearest_station'), train__name=name)
        serial=CurrentStationGetSerializer(data)
        return Response(serial.data, status=200)

    def patch(self, request, name):
        instance=get_object_or_404(CurrentStatus.objects.select_related('train'), train__name=name)
        serial=CurrentStationSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        return Response(serial.errors, status=400)