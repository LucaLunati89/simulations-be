from rest_framework import serializers
from ..models.simulation_model import Simulation

class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = "__all__"