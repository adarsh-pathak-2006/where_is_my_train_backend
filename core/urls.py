from django.urls import path
from .views import CurrentStatusAPI

urlpatterns = [
    path('current-status/', CurrentStatusAPI.as_view())
]
