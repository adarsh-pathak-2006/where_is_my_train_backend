from django.db import models
from station.models import Station
from trains.models import Train

class CurrentStatus(models.Model):
    train=models.OneToOneField(Train, on_delete=models.CASCADE)
    previous_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='previous_station_trains', null=True)
    upcoming_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='next_station_trains', null=True)
    nearest_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_at_nearest_station', null=True)
    distance_from_nearest_station=models.IntegerField(default=0)
    has_started=models.BooleanField(default=False)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.train.name


