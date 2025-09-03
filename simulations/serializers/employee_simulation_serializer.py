from rest_framework import serializers
from ..models.employee_simulation_model import  EmployeeSimulation

class EmployeeSimulationSerializer(serializers.ModelSerializer):
    gross_salary = serializers.SerializerMethodField()
    base_cost = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeSimulation
        fields = ["id", "gross_salary", "tax_rate", "contract_months", "base_cost"]

    def get_gross_salary(self, obj):
        # restituisce già formattato con virgole e due decimali
        return obj.formatted_gross_salary

    def get_base_cost(self, obj):
        return obj.formatted_base_cost