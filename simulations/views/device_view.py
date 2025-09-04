
from rest_framework import generics
from ..models.device_model import  Device
from ..serializers.device_serializer import DeviceSerializer

class GetAllDevices(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer