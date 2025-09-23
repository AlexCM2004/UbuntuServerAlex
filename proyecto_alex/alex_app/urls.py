from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.suma, name="suma"),
    path("", views.resta, name="resta"),
    path("<str:name>", views.saludo, name="saludo")
]