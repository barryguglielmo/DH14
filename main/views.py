#main/views.py


from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'home.html')

def Final_Project(request):
    return render(request, 'Final_Project.html')
	
def home(request):
    return render(request, 'home.html')
	
def stacked_line(request):
    return render(request, 'graphs/stacked_line.html')

def doughnut(request):
    return render(request, 'graphs/doughnut.html')

def area(request):
    return render(request, 'graphs/area.html')

def about(request):
    return render(request, 'about.html')
	
	
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

