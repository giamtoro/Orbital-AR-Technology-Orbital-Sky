from django.db import models

# Create your models here.
class user(models.Model):
    Name= models.CharField(max_length=30)
    Password= models.CharField(max_length=30)
    User_id= models.CharField(max_length=30)

class devce(models.Model):
    Id= models.CharField(max_length=30)
    Devce_name= models.CharField(max_length=30)

class satellite(models.Model):
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    EarthLimbAngle=models.FloatField()
    Name= models.CharField(max_length=30)
    Detector= models.CharField(max_length=30)