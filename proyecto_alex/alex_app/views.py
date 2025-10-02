from django.shortcuts import render
from django.http import HttpResponse
from models import Task

# Create your views here.

def index(request):
	return render(request, "alex_app/index.html")

def saludo (request, nombre):
	return render(request, "alex_app/saludo.html",{"nombre" : nombre.capitalize()})

tasks = ["foo", "bar", "baz"]

def tasks_index (request):
	return render(request, "myapp/tasks_index.html", {
		"tasks": tasks})

def tasks_add (request):
	if request.method == "POST":
		task = request.POST.get("task")
		if task:
			task.append(task)
		return HttpResponseRedirect(reverse("tasks_index"))
	return render(request, "myapp/task_add.html")

def tasks_admin_list (request):
	task = Task.objects.all().order_by("created at")
	return render(request, "myapp/task_admin_list.html", {
		"tasks": task
	})