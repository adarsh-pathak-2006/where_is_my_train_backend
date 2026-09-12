from django.db import models
from station.models import Station

class Train(models.Model):
    name=models.CharField(max_length=300)
    starting_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_starting')
    ending_station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_ending')
    train_type=models.CharField(max_length=15, choices=[('SUPERFAST', 'SUPERFAST'), ('PASSENGER', 'PASSENGER'), ('MEMU', 'MEMU'), ('EXPRESS', 'EXPRESS')])
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TrainStation(models.Model):
    train=models.ForeignKey(Train, on_delete=models.CASCADE, related_name='stations')
    station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_stations')
    stopping_time=models.DurationField()
    distance_from_origin=models.PositiveIntegerField(default=0)
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"train {self.train.name} at {self.station.name}"

