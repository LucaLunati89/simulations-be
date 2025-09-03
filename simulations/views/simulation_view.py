from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from simulations.models.simulation_model import Simulation 
from simulations.serializers.simulation_serializer import SimulationSerializer
from ..enums.simulation_status import SimulationStatus

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

# Paginated search by Employee ID (employee_id obbligatorio)
class SimulationsByEmployee(APIView, PageNumberPagination):
    page_size = 10  # Numero di simulazioni per pagina

    def get(self, request):
        employee_simulation_id = request.query_params.get('employee_simulation_id')
        if not employee_simulation_id:
            return Response(
                {"error": "employee_simulation_id è obbligatorio"},
                status=status.HTTP_400_BAD_REQUEST
            )

        simulations = Simulation.objects.filter(employee_simulation__id=employee_simulation_id).order_by('-created_at')
        results = self.paginate_queryset(simulations, request, view=self)
        serializer = SimulationSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
# 4. Update Simulation Status
class UpdateSimulationStatus(APIView):
    def patch(self, request, pk):
        simulation = get_object_or_404(Simulation, pk=pk)
        
        if simulation.status == SimulationStatus.COMPLETED:
            return Response(
                {"error": "Lo stato 'COMPLETED' non può essere modificato."},
                status=status.HTTP_400_BAD_REQUEST
            )

        new_status = request.data.get("status")
        if not new_status:
            return Response(
                {"error": "Il campo 'status' è obbligatorio."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verifica che lo status sia valido
        if new_status not in SimulationStatus.values:
            return Response(
                {"error": f"Stato non valido. Valori consentiti: {SimulationStatus.values}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        simulation.status = new_status
        simulation.save()
        serializer = SimulationSerializer(simulation)
        return Response(serializer.data, status=status.HTTP_200_OK)
