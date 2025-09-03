""" from django.urls import path, include

urlpatterns = [
    # path("devices/", GetAllDevices.as_view(), name="get-devices"),
    # path('simulation-device/<int:simulation_id>/', ListSimulationDevices.as_view(), name='list_simulation_devices'),
    # path("simulation-device/add/", AddSimulationDevice.as_view(), name="add-simulation-device"),
    # path("simulation-device/<int:pk>/update", UpdateSimulationDevice.as_view(), name="update-simulation-device"),
    # path("simulation-device/<int:pk>/delete/", DeleteSimulationDevice.as_view(), name="delete-simulation-device"),
    path("employee-simulation/", include("simulations.urls.employee_simulation_url")),
    path("simulation/", include(("simulations.urls.simulation", "simulation"))),
]
 """