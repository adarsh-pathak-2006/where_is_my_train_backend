from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import CurrentStatus
from trains.serializers import TrainSerializer
from station.serializers import StationSerializer
from trains.models import Train
from station.models import Station

class CurrentStationGetSerializer(ModelSerializer):
    train=TrainSerializer(read_only=True)
    previous_station=StationSerializer(read_only=True)
    upcoming_station=StationSerializer(read_only=True)
    nearest_station=StationSerializer(read_only=True)
    class Meta:
        model=CurrentStatus
        fields='__all__'
        read_only_fields=['distance_from_nearest_station', 'has_started', 'updated_on']


class CurrentStationSerializer(ModelSerializer):
    train=PrimaryKeyRelatedField(queryset=Train.objects.all())
    previous_station=PrimaryKeyRelatedField(queryset=Station.objects.all())
    upcoming_station=PrimaryKeyRelatedField(queryset=Station.objects.all())
    nearest_station=PrimaryKeyRelatedField(queryset=Station.objects.all())
    class Meta:
        model=CurrentStatus
        fields='__all__'