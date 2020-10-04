from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

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

def satellite(request):
    return render(request, 'satellite.html')

def geo(request):
    return render(request, 'geo.html')