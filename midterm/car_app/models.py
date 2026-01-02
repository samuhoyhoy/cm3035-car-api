from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    body_style = models.CharField(max_length=100, null=True, blank=True)
    segment = models.CharField(max_length=255, null=True, blank=True)
    production_year = models.IntegerField(null=True, blank=True)
    cylinders = models.CharField(max_length=10)
    displacement = models.FloatField(null=True, blank=True)
    horsepower = models.CharField(max_length=50, default="N/A")
    torque_nm = models.CharField(max_length=50, default="N/A")
    fuel = models.CharField(max_length=50, null=True, blank=True)
    top_speed = models.CharField(max_length=50, default="N/A")
    acceleration = models.CharField(max_length=20, default="N/A")
    drive_type = models.CharField(max_length=50, null=True, blank=True)
    gearbox = models.CharField(max_length=50, null=True, blank=True)
    unladen_weight = models.CharField(max_length=50, default="N/A")

def __str__(self):
    return f"{self.company} {self.model} ({self.production_year})"