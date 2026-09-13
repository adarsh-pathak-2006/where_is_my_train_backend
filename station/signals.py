from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Station
from wimt.cache_key import station_cache_key
from django.core.cache import cache

@receiver(post_save, sender=Station)
def cache_invalidation_in_station(sender, instance, created, **kwargs):
    for i in range(1, 101):
        cache.delete(station_cache_key(pageno=i))