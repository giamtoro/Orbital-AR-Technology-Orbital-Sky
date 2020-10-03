from django.db import models

# Create your models here.
class user(models.Model):
    Name= models.CharField(max_length=30)
    Password= models.CharField(max_length=30)
    Image=models.ImageField()#add imMAGE DEFAULT

class satellite(models.Model):
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    EarthLimbAngle=models.FloatField()
    Name= models.CharField(max_length=30)
    Detector= models.CharField(max_length=30)