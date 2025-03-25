# routes/models.py
from django.db import models

class Route(models.Model):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    distance = models.FloatField()
    duration = models.FloatField()
    
    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location}"
