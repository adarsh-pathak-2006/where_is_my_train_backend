from rest_framework.serializers import ModelSerializer
from .models import TrainStation, Train
from station.serializers import StationSerializer


class TrainSerializer(ModelSerializer):
    starting_station=StationSerializer(read_only=True)
    ending_station=StationSerializer(read_only=True)
    class Meta:
        model=Train
        fields='__all__'
        read_only_fields=['added_on']

class TrainStationSerializer(ModelSerializer):
    class Meta:
        model=TrainStation
        fields='__all__'
        read_only_fields=['added_on']
