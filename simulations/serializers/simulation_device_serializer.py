from rest_framework import serializers
from ..models.device_model import Device
from ..serializers.device_serializer import DeviceSerializer
from ..models.simulation_device_model import SimulationDevice

class SimulationDeviceSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    device_id = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        source="device",
        write_only=True
    )
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = SimulationDevice
        fields = ["id", "simulation", "device", "device_id", "months", "total_cost"]

    def get_total_cost(self, obj):
        return obj.formatted_total_cost
