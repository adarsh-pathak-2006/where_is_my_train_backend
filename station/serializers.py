from rest_framework.serializers import ModelSerializer
from .models import Station

class StationSerializer(ModelSerializer):
    class Meta:
        model=Station
        fields='__all__'
        read_only_fields=['added_on']