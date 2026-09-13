from django.dispatch import receiver
from wimt.cache_key import train_all_station_cache_key, train_list_cache_key
from .models import TrainStation, Train
from django.db.models.signals import post_save
from django.core.cache import cache

@receiver(post_save, sender=Train)
def train_list_cache_invalidation(sender, instance, created, **kwargs):
    for i in range(1, 101):
        cache.delete(train_list_cache_key(pageno=i))

@receiver(post_save, sender=TrainStation)
def TrainStationCacheInvalidation(sender, instance, created, **kwargs):
    cache.delete(train_all_station_cache_key(instance.id))