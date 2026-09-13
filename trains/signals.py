from django.dispatch import receiver
from wimt.cache_key import train_all_station_cache_key
from .models import TrainStation
from django.db.models.signals import post_save
from django.core.cache import cache

@receiver(post_save, sender=TrainStation)
def TrainStationCacheInvalidation(sender, instance, created, **kwargs):
    cache.delete(train_all_station_cache_key(instance.id))