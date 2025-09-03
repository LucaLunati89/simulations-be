from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from simulations.models.simulation_model import Simulation 
from simulations.serializers.simulation_serializer import SimulationSerializer

# 1. Find Simulation by ID
class FindSimulationById(APIView):
    def get(self, request, pk):
        simulation = get_object_or_404(Simulation, pk=pk)
        serializer = SimulationSerializer(simulation)
        return Response(serializer.data)

# 2. Create Simulation
class CreateSimulation(APIView):
    def post(self, request):
        serializer = SimulationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)