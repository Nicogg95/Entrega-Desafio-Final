from unicodedata import name
from django.urls import path, include
from AppCoder import views
from ProyectoFP.urls import * 


urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("clientes/", views.clientes,name = "clientes"),
    path("buscar/", views.buscar,name = "buscar"),
    path("buscardoc/", views.buscardoc,name = "buscardoc"),
    path("registro/", views.registrou, name= "registro"),
    path("resultado/", views.resultado, name= "resultado"),


] 
