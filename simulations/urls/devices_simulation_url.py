from django.urls import path
from simulations.views.devices_simulation_view import (ListSimulationDevices, AddSimulationDevice, UpdateSimulationDevice, DeleteSimulationDevice)

urlpatterns = [
    path('<int:simulation_id>/', ListSimulationDevices.as_view(), name='list_simulation_devices'),
    path("add/", AddSimulationDevice.as_view(), name="add-simulation-device"),
    path("<int:pk>/update", UpdateSimulationDevice.as_view(), name="update-simulation-device"),
    path("<int:pk>/delete/", DeleteSimulationDevice.as_view(), name="delete-simulation-device"),
]
