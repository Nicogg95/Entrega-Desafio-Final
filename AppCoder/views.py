from ast import Return
from django.shortcuts import render
from django.http import HttpResponse, request
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):

    return render (request,"AppCoder/inicio.html")

def clientes(request):

    return render (request,"clientes.html")

def resultado(request):

    return render (request,"AppCoder/resultado.html")

def buscardoc(request):

    return render (request,"AppCoder/buscardoc.html")

def buscar(request):

    if request.GET["documento"]:

        busqueda= request.GET["documento"]
        clientes = Clientes.objects.filter(documento_icontains=busqueda)

        return render(request, "resultadobus.html", {"clientes": clientes, "busqueda": busqueda})
    else:
        mensaje = "No envio los datos." 
    
    return HttpResponse (mensaje)

def registrou(request):

    if request.method =="POST":

        formulario1= Clienteregistrou(request.POST)

        print(formulario1)

        if formulario1.is_valid():

            info= formulario1.cleaned_data

            clientef = Clientes(nombre=info["nombre"], apellido=info["apellido"], documento=info["documento"], telefono=info["telefono"], email=info["email"], pais =info["pais"], provincia=info["provincia"], localidad =info["localidad"])

            clientef.save()

            return render (request, "AppCoder/resultado.html")

    else: 
        formulario1= Clienteregistrou()  

    
    return render (request,"AppCoder/registrou.html", {"formulario1": formulario1})


