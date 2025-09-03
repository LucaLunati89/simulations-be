from django.db import models
from .employee_simulation_model import EmployeeSimulation
from ..enums.simulation_status import SimulationStatus

class Simulation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    employee_simulation = models.ForeignKey(
        EmployeeSimulation, on_delete=models.CASCADE, related_name="simulations"
    )

    status = models.CharField(
        max_length=10,
        choices=SimulationStatus.choices,
        default=SimulationStatus.CREATED
    )
    def __str__(self):
        return f"{self.name or 'Simulation'}: Emp {self.employee_simulation.id}"