""" from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Simulation, EmployeeSimulation, Device, SimulationDevice
from .serializers import (
    SimulationSerializer,
    EmployeeSimulationSerializer,
    DeviceSerializer,
    SimulationDeviceSerializer,
)

# 1. Find Simulation by ID
class FindSimulationById(APIView):
    def get(self, request, pk):
        simulation = get_object_or_404(Simulation, pk=pk)
        serializer = SimulationSerializer(simulation)
        return Response(serializer.data)


# 2. Find EmployeeSimulation by ID
class FindEmployeeSimulationById(APIView):
    def get(self, request, pk):
        emp_sim = get_object_or_404(EmployeeSimulation, pk=pk)
        serializer = EmployeeSimulationSerializer(emp_sim)
        return Response(serializer.data)


# 3. Get All Devices
class GetAllDevices(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# 4. Add SimulationDevice
class AddSimulationDevice(APIView):
    def post(self, request):
        simulation_id = request.data.get("simulation_id")
        device_id = request.data.get("device_id")

        simulation = get_object_or_404(Simulation, pk=simulation_id)
        device = get_object_or_404(Device, pk=device_id)

        if SimulationDevice.objects.filter(simulation_id=simulation_id, device_id=device_id).exists():
            return Response({"error": "Device already added"}, status=status.HTTP_409_CONFLICT)

        # Default months = employee contract months
        employee_sim = EmployeeSimulation.objects.filter(simulation=simulation).first()
        if not employee_sim:
            return Response({"error": "EmployeeSimulation not found for this Simulation"}, status=400)

        sim_device = SimulationDevice.objects.create(
            simulation=simulation, device=device, months=employee_sim.contract_months
        )

        return Response(SimulationDeviceSerializer(sim_device).data, status=201)



# 5. Patch SimulationDevice (update months)
class UpdateSimulationDevice(APIView):
    def patch(self, request, pk):
        sim_device = get_object_or_404(SimulationDevice, pk=pk)
        months = request.data.get("months")

        if not months:
            return Response({"error": "Months field required"}, status=400)

        employee_sim = EmployeeSimulation.objects.filter(simulation=sim_device.simulation).first()
        if int(months) < 1 or int(months) > employee_sim.contract_months:
            return Response({"error": "Invalid months value"}, status=400)

        sim_device.months = months
        sim_device.save()

        return Response(SimulationDeviceSerializer(sim_device).data)


# 6. Delete SimulationDevice
class DeleteSimulationDevice(APIView):
    def delete(self, request, pk):
        sim_device = get_object_or_404(SimulationDevice, pk=pk)
        sim_device.delete()
        return Response({"message": "SimulationDevice deleted"}, status=204)

# 7. List SimulationDevices by Simulation ID
class ListSimulationDevices(APIView):
    def get(self, request, simulation_id):
        devices = SimulationDevice.objects.filter(simulation_id=simulation_id)
        serializer = SimulationDeviceSerializer(devices, many=True)
        return Response(serializer.data, status=200) """