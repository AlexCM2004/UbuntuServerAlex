from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random
from .models import Task

# Create your views here.

def index(request):
	return render(request, "alex_app/index.html")

def index2(request):
    return render(request, "alex_app/index2.html")

def index_html(request):
    return render(request, "alex_app/index.html")

def indextest(request):
    return render(request, 'alex_app/indextest.html')

def about(request):
    return render(request, "alex_app/about.html")

def saludo (request, nombre):
	return render(request, "alex_app/saludo.html",{"nombre" : nombre.capitalize()})

tasks = ["foo", "bar", "baz"]

def tasks_index (request):
	return render(request, "alex_app/tasks_index.html", {
		"tasks": tasks})

def tasks_add (request):
	if request.method == "POST":
		task = request.POST.get("task")
		if task:
			task.append(task)
		return HttpResponseRedirect(reverse("tasks_index"))
	return render(request, "alex_app/task_add.html")

def tasks_admin_list (request):
	task = Task.objects.all().order_by("created at")
	return render(request, "alex_app/task_admin_list.html", {
		"tasks": task
	})