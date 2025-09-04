from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models.simulation_model import Simulation
from ..models.employee_simulation_model import EmployeeSimulation
from ..models.device_model import Device
from ..models.simulation_device_model import SimulationDevice
from ..serializers.simulation_device_serializer import SimulationDeviceSerializer


# 4. Add SimulationDevice
class AddSimulationDevice(APIView):
    def post(self, request):
        simulation_id = request.data.get("simulation_id")
        device_id = request.data.get("device_id")

        simulation = get_object_or_404(Simulation, pk=simulation_id)
        device = get_object_or_404(Device, pk=device_id)

        if SimulationDevice.objects.filter(simulation=simulation, device=device).exists():
            return Response({"error": "Device already added"}, status=status.HTTP_409_CONFLICT)

        if simulation.status == "COMPLETED":
            return Response(
                {"error": "Cannot add device to a COMPLETED simulation"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Default months = employee contract months
        employee_sim = simulation.employee_simulation
        if not employee_sim:
            return Response({"error": "EmployeeSimulation not found for this Simulation"}, status=400)

        sim_device = SimulationDevice.objects.create(
            simulation=simulation,
            device=device,
            months=employee_sim.contract_months
        )

        return Response(SimulationDeviceSerializer(sim_device).data, status=status.HTTP_201_CREATED)


# 5. Patch SimulationDevice (update months)
class UpdateSimulationDevice(APIView):
    def patch(self, request, pk):
        sim_device = get_object_or_404(SimulationDevice, pk=pk)
        months = request.data.get("months")

        if not months:
            return Response({"error": "Months field required"}, status=status.HTTP_400_BAD_REQUEST)

        employee_sim = sim_device.simulation.employee_simulation
        if not employee_sim:
            return Response({"error": "EmployeeSimulation not found for this Simulation"}, status=400)

        if int(months) < 1 or int(months) > employee_sim.contract_months:
            return Response({"error": "Invalid months value"}, status=status.HTTP_400_BAD_REQUEST)

        sim_device.months = int(months)
        sim_device.save()

        return Response(SimulationDeviceSerializer(sim_device).data, status=status.HTTP_200_OK)


# 6. Delete SimulationDevice
class DeleteSimulationDevice(APIView):
    def delete(self, request, pk):
        sim_device = get_object_or_404(SimulationDevice, pk=pk)
        sim_device.delete()
        return Response({"message": "SimulationDevice deleted"}, status=status.HTTP_204_NO_CONTENT)


# 7. List SimulationDevices by Simulation ID
class ListSimulationDevices(APIView):
    def get(self, request, simulation_id):
        devices = SimulationDevice.objects.filter(simulation_id=simulation_id)
        serializer = SimulationDeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
