from django.shortcuts import render
from django.http import HttpResponse
from models import Task

# Create your views here.

def index(request):
	return render(request, "alex_app/index.html")

def saludo (request, nombre):
	return render(request, "alex_app/saludo.html",{"nombre" : nombre.capitalize()})