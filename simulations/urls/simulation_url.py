from django.urls import path
from simulations.views.simulation_view import (FindSimulationById, CreateSimulation, SimulationsByEmployee, UpdateSimulationStatus)

urlpatterns = [
    path("<int:pk>/", FindSimulationById.as_view(), name="find-simulation"),
    path("create/", CreateSimulation.as_view(), name="create-simulation"),
    path("", SimulationsByEmployee.as_view(), name="list-simulations"),
    path("<int:pk>/status", UpdateSimulationStatus.as_view(), name="update-simulation"),
]
