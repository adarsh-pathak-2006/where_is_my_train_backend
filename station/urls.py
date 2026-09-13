from django.urls import path
from .views import StationAPI, TrainOnStationAPI

urlpatterns = [
    path('stations/', StationAPI.as_view()),
    path("stations/<int:pk>/", TrainOnStationAPI.as_view())
]
