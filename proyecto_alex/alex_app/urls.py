from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
    path('index2/', views.index2, name='index2'),
    path('about/', views.about, name='about'),
    path('indextest/', views.indextest, name='indextest'),
    # Tasks demo
    path('tasks/', views.tasks_index, name='tasks_index'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('admin-tasks/', views.tasks_admin_list, name='tasks_admin_list'),
]