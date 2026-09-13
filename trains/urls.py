from django.urls import path
from .views import AllTrainAPI, TrainStationAPI, TrainEnquiryBasedOnStationAPI

urlpatterns = [
    path('trains/', AllTrainAPI.as_view()),
    path('train/<int:pk>/', TrainStationAPI.as_view()),
    path('train-enquiry/', TrainEnquiryBasedOnStationAPI.as_view())
]
