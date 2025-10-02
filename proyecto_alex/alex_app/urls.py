from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:nombre>", views.saludo, name="saludo"),
    path("tasks", views.tasks_index, name="tasks_index"),
    path("tasks/add", views.tasks_add, name="tasks_add"),
    path("admin-tasks", views.task_admin_list, name="tasks_admin_list"),
    path("menu", views.index2, name="index2")
]