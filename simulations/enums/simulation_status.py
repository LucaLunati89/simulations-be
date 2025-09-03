from django.db import models

class SimulationStatus(models.TextChoices):
    CREATED = "CREATED", "Created"
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"