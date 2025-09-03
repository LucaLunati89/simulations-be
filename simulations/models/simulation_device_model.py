from django.db import models
from decimal import Decimal
from .device_model import Device
from .simulation_model import Simulation

class SimulationDevice(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    months = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["simulation", "device"],
                name="uniq_simulation_device"
            )
        ]
        
    def total_cost(self):
        return self.device.monthly_cost * Decimal(self.months)

    @property
    def formatted_total_cost(self):
        return f"{self.total_cost():,.2f}"

    def __str__(self):
        return f"{self.device.model} for {self.months} months"
