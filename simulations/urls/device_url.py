from django.urls import path
from simulations.views.device_view import GetAllDevices

urlpatterns = [
    path("", GetAllDevices.as_view(), name="list-devices"),
]
