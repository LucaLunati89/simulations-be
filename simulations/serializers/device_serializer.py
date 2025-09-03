from rest_framework import serializers
from ..models.device_model import Device

class DeviceSerializer(serializers.ModelSerializer):
    monthly_cost = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = ["id", "model", "monthly_cost", "brand"]

    def get_monthly_cost(self, obj):
        return f"{obj.monthly_cost:,.2f}"