from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Team


def home(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request,'pages/about.html',data )

def cars(request):
    return render(request,'pages/cars.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')

# Create your views here.
