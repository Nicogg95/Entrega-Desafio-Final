from django.shortcuts import render
from django.http import HttpResponse, request
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):

    return render (request,"AppCoder/inicio.html")
    

def clientes(request):

    return render (request,"AppCoder/clientes.html")


def resultado(request):

    return render (request,"AppCoder/resultado.html")


def buscar(request):

    return render (request,"AppCoder/buscar.html")


def busquedacliente(request):

    if "doc" in request.GET:

        documento = request.GET["doc"]

    else:

        documento = False


    if documento:
     
        nombre= Clientes.objects.filter(documento__icontains=documento)

        return render (request,"AppCoder/busquedacliente.html", {"nombres": nombre,  "documento": documento})

    else:
            respuesta= "No ingreso ningun caracter o un caracter valido, intente nuevamente"

    return render(request, "AppCoder/busquedacliente.html", {"respuesta": respuesta})



def registro(request):

    if request.method =="POST":

        formulario1= Clienteregistro(request.POST)

        print(formulario1)

        if formulario1.is_valid():

            info= formulario1.cleaned_data

            clientef = Clientes(nombre=info["nombre"], apellido=info["apellido"], documento=info["documento"], telefono=info["telefono"], email=info["email"], pais =info["pais"], provincia=info["provincia"], localidad =info["localidad"])

            clientef.save()

            return render (request,"AppCoder/resultado.html")

    else: 

        formulario1= Clienteregistro()  
        return render (request,"AppCoder/registro.html", {"formulario1": formulario1})


