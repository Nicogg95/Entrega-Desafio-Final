from unicodedata import name
from django.urls import path, include
from AppCoder import views
from .urls import * 


urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("clientes/", views.clientes,name = "clientes"),
    path("registro/", views.registro, name= "registro"),
    path("resultado/", views.resultado, name= "resultado"),
    path("buscar/", views.buscar, name = "buscar"),
    path("resultadobus/", views.resultadobus, name = "resultadobus"),
] 
