from django.db import models

# Create your models here.

class satellite(models.Model):
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    EarthLimbAngle=models.FloatField()
    Name= models.CharField(max_length=30)
    Detector= models.CharField(max_length=30)