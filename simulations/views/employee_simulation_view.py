from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from ..models.employee_simulation_model import EmployeeSimulation
from ..serializers.employee_simulation_serializer import EmployeeSimulationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

# Ricerca una simulazione dipendente per ID
class FindEmployeeSimulationById(APIView):
    def get(self, request, pk):
        emp_sim = get_object_or_404(EmployeeSimulation, pk=pk)
        serializer = EmployeeSimulationSerializer(emp_sim)
        return Response(serializer.data)

# Ricerca paginata di simulazioni dipendenti con filtri e ordinamento su gross_salary
class EmployeeSimulationListView(APIView):
    """
    Lista paginata di EmployeeSimulation con filtro per gross_salary e ordinamento.
    Query params:
        - min_salary: float (opzionale)
        - max_salary: float (opzionale)
        - order_by: "gross_salary" o "-gross_salary" (opzionale, default id asc)
        - page: numero pagina (default 1)
        - page_size: numero elementi per pagina (default 10)
    """

    def get(self, request):
        queryset = EmployeeSimulation.objects.all()

        # Filtri
        min_salary = request.GET.get("min_salary")
        max_salary = request.GET.get("max_salary")
        if min_salary:
            queryset = queryset.filter(gross_salary__gte=min_salary)
        if max_salary:
            queryset = queryset.filter(gross_salary__lte=max_salary)

        # Ordinamento
        order_by = request.GET.get("order_by", "id")
        if order_by in ["gross_salary", "-gross_salary", "id", "-id"]:
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by("id")

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = request.GET.get("page_size", 10)
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = EmployeeSimulationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)