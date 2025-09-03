from django.urls import path
from simulations.views.employee_simulation_view import (FindEmployeeSimulationById, EmployeeSimulationListView)

urlpatterns = [
    path("<int:pk>/", FindEmployeeSimulationById.as_view(), name="find-employee-simulation"),
    path("", EmployeeSimulationListView.as_view(), name="list-employee-simulations"),
]
