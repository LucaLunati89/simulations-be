from rest_framework import serializers
from ..models.device_model import Device
from ..models.simulation_model import Simulation
from ..models.simulation_device_model import SimulationDevice
from ..serializers.device_serializer import DeviceSerializer

class SimulationDeviceSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    device_id = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        source="device",
        write_only=True
    )
    simulation_id = serializers.PrimaryKeyRelatedField(
        queryset=Simulation.objects.all(),
        source="simulation",
        write_only=True
    )
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = SimulationDevice
        fields = [
            "id",
            "simulation",      # restituisce i dati completi della Simulation se serve
            "simulation_id",   # input/output come PK
            "device",          # nested serializer del Device
            "device_id",       # input/output come PK
            "months",
            "total_cost",
        ]

    def get_total_cost(self, obj):
        return obj.formatted_total_cost
