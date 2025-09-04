from django.urls import include, path

urlpatterns = [
    path("simulations/", include("simulations.urls.simulation_url")),
    path("employee-simulations/", include("simulations.urls.employee_simulations_url")),
    path("devices/", include("simulations.urls.device_url")),
    path("devices-simulation/", include("simulations.urls.devices_simulation_url")),
]
