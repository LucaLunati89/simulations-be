from django.contrib import admin
from .models.device_model import Device
from .models.simulation_device_model import SimulationDevice
from .models.simulation_model import Simulation
from .models.employee_simulation_model import EmployeeSimulation
admin.site.register(Simulation)
admin.site.register(EmployeeSimulation)
admin.site.register(Device)
admin.site.register(SimulationDevice)
