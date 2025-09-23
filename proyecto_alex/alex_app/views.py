from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, world!")

def suma(request):
	return HttpResponse(1 + 2)

def resta(request):
	return HttpResponse(5 - 3)

def saludo (request, nombre):
	return render(request, "alex_app/saludo.html",{"nombre" : nombre.capitalize()})