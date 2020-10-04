from django.shortcuts import render
from django.http import HttpResponse
from .models import Satellite,Decrittor
import json
# Create your views here.
db_satellite=Satellite
db_Decrittor=Decrittor

def home(request):
    return render(request, 'home.html')

def vr(request):
    x=12
    y=-10
    z=15
    context= {
        'x': x,
        'y': y,
        'z': z,
        }
    return render(request, 'virtual.html',context)

def geo(request):
    return render(request, 'geo.html')


def read_json():
    with open('data.json') as json_file: 
        data = json.load(json_file) 
    
        # for reading nested data [0] represents 
        # the index value of the list 
        print(data['people1'][0]) 
        
        # for printing the key-value pair of 
        # nested dictionary for looop can be used 
        print("\nPrinting nested dicitonary as a key-value pair\n") 
        for i in data['people1']: 
            print("Name:", i['name']) 
            print("Website:", i['website']) 
            print("From:", i['from']) 
            print()

def add_Satellite(yaw,roll,pitch,x,y,z,name,Id):
    db_satellite(
        yaw=yaw,roll=roll,pitch=pitch,x=x,y=y,z=z,name=name,Id=Id
        )
    db_satellite.save()

def add_Decrittor(descrizion,name,tipo):
    db_Decrittor(descrizion=descrizion,name=name,tipo=tipo)
    db_Decrittor.save()

def get_satellite(name,Id):
    tmp=db_satellite.objects.values()
    if tmp.__contains__(name) & tmp.__contains__(Id):
        return tmp.filter(name=name,Id=Id)

def get_Decrittor(name,tipo):
    tmp=db_satellite.objects.values()
    if tmp.__contains__(name) & tmp.__contains__(tipo):
        return tmp.filter(name=name,tipo=tipo)


