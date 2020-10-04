from django.db import models

# Create your models here.

class Satellite(models.Model):
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    EarthLimbAngle=models.FloatField()
    Name= models.CharField(max_length=30)
    Detector= models.CharField(max_length=30)

class Decrittor(models.Model):
    Name= models.CharField(max_length=30)
    Detector= models.CharField(max_length=30)
    descrizion= models.CharField(max_length=500)