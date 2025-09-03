from django.urls import path
from simulations.views.simulation_view import (FindSimulationById, CreateSimulation)

urlpatterns = [
    path("<int:pk>/", FindSimulationById.as_view(), name="find-simulation-test"),
    path("create/", CreateSimulation.as_view(), name="create-simulation"),
]
