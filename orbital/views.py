from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def vr(request):
    return render(request, 'virtual.html')

def satellite(request):
    return render(request, 'satellite.html')

def geo(request):
    return render(request, 'geo.html')