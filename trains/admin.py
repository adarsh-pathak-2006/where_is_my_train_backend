from django.contrib import admin
from .models import Train, TrainStation

admin.site.register(TrainStation)
admin.site.register(Train)
