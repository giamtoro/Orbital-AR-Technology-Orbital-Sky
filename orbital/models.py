from django.db import models

# Create your models here.

class Satellite(models.Model):
    yaw= models.FloatField()
    roll= models.FloatField()
    pitch= models.FloatField()
    x= models.FloatField()
    y= models.FloatField()
    z= models.FloatField()
    Name= models.CharField(max_length=30)
    Id= models.IntegerField()

class Decrittor(models.Model):
    Name= models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)
    descrizion= models.CharField(max_length=500)