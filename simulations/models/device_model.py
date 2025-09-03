from django.db import models

class Device(models.Model):
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    monthly_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model