from django.db import models

# Create your models here.

class user(models.Model):
    name= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    user_id= models.CharField(max_length=30)

class devce(models.Model):
    id= models.CharField(max_length=30)
    devce_name= models.CharField(max_length=30)
