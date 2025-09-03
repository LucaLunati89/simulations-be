from django.db import models
from decimal import Decimal

class EmployeeSimulation(models.Model):
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)  # annuale
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2)  # es: 0.31 = 31%
    contract_months = models.PositiveIntegerField()

    def base_cost(self):
        """
        Ritorna il costo totale del dipendente in base alla durata del contratto.
        Formula:
        (stipendio lordo annuo * (mesi_contratto / 12)) * (1 + tax_rate)
        """
        proportion = Decimal(self.contract_months) / Decimal(12)
        return self.gross_salary * proportion * (Decimal(1) + self.tax_rate)

    @property
    def formatted_gross_salary(self):
        return f"{self.gross_salary:,.2f}"

    @property
    def formatted_base_cost(self):
        return f"{self.base_cost():,.2f}"

    def __str__(self):
        return f"EmployeeSimulation {self.id}"