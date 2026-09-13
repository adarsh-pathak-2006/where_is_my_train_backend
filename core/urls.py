from django.urls import path
from .views import CurrentStatusAPI

urlpatterns = [
    path('current-status/<str:name>/', CurrentStatusAPI.as_view())
]
