from django.db import models
from station.models import Station
from trains.models import Train

class CurrentStatus(models.Model):
    train=models.OneToOneField(Train, on_delete=models.CASCADE)
    previous_station=models.ForeignKey(Station, on_delete=models.CASCADE, null=True)
    upcoming_station=models.ForeignKey(Station, on_delete=models.CASCADE, null=True)
    nearest_station=models.ForeignKey(Station, on_delete=models.CASCADE, null=True)
    distance_from_nearest_station=models.IntegerField(default=0)
    has_started=models.BooleanField(default=False)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.train.name


