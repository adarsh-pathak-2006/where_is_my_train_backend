from django.db import models
from station.models import Station
from trains.models import Train, TrainStation

class CurrentStatus(models.Model):
    train=models.OneToOneField(Train, on_delete=models.CASCADE)
    previous_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='previous_station_trains', null=True)
    upcoming_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='next_station_trains', null=True)
    nearest_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_at_nearest_station', null=True)
    distance_from_nearest_station=models.IntegerField(default=0)
    has_started=models.BooleanField(default=False)
    updated_on=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.previous_station is not None and not TrainStation.objects.select_related('train', 'station').filter(models.Q(train=self.train), models.Q(station=self.previous_station)).exists():
            raise ValueError("Previous Stations must be in the Train Route Stations")
        if self.upcoming_station is not None and not TrainStation.objects.select_related('train', 'station').filter(models.Q(train=self.train), models.Q(station=self.upcoming_station)).exists():
            raise ValueError("Upcoming Station must be in the Train Route Stations")
        if self.nearest_station is not None and not TrainStation.objects.select_related('train', 'station').filter(models.Q(train=self.train), models.Q(station=self.nearest_station)).exists():
            raise ValueError("nearest station must be in the Train Route Stations")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.train.name


