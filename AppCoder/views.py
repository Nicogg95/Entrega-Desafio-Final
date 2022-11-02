from django.http import HttpResponse, request
from django.shortcuts import render
from django.urls import reverse
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def inicio(request):

    return render (request,"AppCoder/inicio.html")


#################################################################


def about(request):

    return render (request,"AppCoder/about.html")


#################################################################


def usuario(request):

    return render (request,"AppCoder/usuario.html")


#################################################################


def resultado(request):

    return render (request,"AppCoder/resultado.html")


#################################################################


def buscar(request):

    return render (request,"AppCoder/buscar.html")


#################################################################


def busquedajuego(request):

    if "doc" in request.GET:

        nombre = request.GET["doc"]

    else:

        nombre = False


    if nombre:
     
        nombre= Juego.objects.filter(nombre__iexact=nombre)
        aniosalida= Juego.objects.filter(nombre__iexact=nombre)
        genero= Juego.objects.filter(nombre__iexact=nombre)

        return render (request,"AppCoder/busquedaJuego.html", {"nombres": nombre, "añosalida": aniosalida, "genero": genero})

    else:

        return render(request, "AppCoder/busquedaJuego.html")

    
#################################################################
    

def registro(request):

    if request.method =="POST":

        datosusuario= Usuariosregistro(request.POST)

        print(datosusuario)

        if datosusuario.is_valid():

            info= datosusuario.cleaned_data

            usuariof = Usuario(nombre=info["nombre"], apellido=info["apellido"], documento=info["documento"], telefono=info["telefono"], email=info["email"], pais =info["pais"], provincia=info["provincia"], localidad =info["localidad"])

            usuariof.save()

            return render (request,"AppCoder/resultado.html")

    else: 

        datosusuario= Usuariosregistro()  
        contexto=  {"datosusuario": datosusuario}
        return render (request,"AppCoder/registro.html",contexto)

    
#################################################################
    

def catalogo(request):

    juegos= Juego.objects.all()

    contexto= {"juegos": juegos}

    return render(request, "AppCoder/catalogo.html", contexto)


#################################################################


def juegoIngreso(request):

    if request.method =="POST":

        datosjuego= Juegosingreso(request.POST)

        print(datosjuego)

        if datosjuego.is_valid():

            info= datosjuego.cleaned_data

            juegof = Juego(titulo=info["titulo"], descripcion=info["descripcion"], genero=info["genero"],  año_de_salida=info["año_de_salida"], tipo_de_juego=info["tipo_de_juego"])

            juegof.save()

            return render (request,"AppCoder/juegoIngreso.html")

    else: 

        datosjuego= Juegosingreso()  
        return render (request,"AppCoder/juegoIngreso.html", {"datosjuego": datosjuego})


#################################################################
    

def actualizarJuego(request, tituloJuego):

    juegof = Juego.objects.get(titulo=tituloJuego)

    if request.method =="POST":

        datosjuego= Juegosingreso(request.POST)

        print(datosjuego)

        if datosjuego.is_valid():

            info= datosjuego.cleaned_data

            juegof.titulo= info["titulo"]
            juegof.descripcion= info["descripcion"]
            juegof.genero= info["genero"]
            juegof.año_de_salida= info["año_de_salida"]
            juegof.tipo_de_juego= info["tipo_de_juego"]

            juegof.save()

            return render (request,"AppCoder/inicio.html")
        
    else: 

        datosjuego= Juegosingreso(initial=
            {"titulo":juegof.titulo,
            "descripcion":juegof.descripcion,
            "genero":juegof.genero,
            "año_de_salida":juegof.año_de_salida,
            "tipo_de_juego":juegof.tipo_de_juego})  
        
        return render (request,"AppCoder/actualizarJuego.html", {"datosjuego": datosjuego, "titulo":tituloJuego})
        
        
#################################################################
        

def eliminarJuego(request, tituloJuego):

    juego= Juego.objects.get(titulo=tituloJuego)
    juego.delete()

    juego= Juego.objects.all()

    contexto={"game":juego}

    return render(request,"AppCoder/catalogo.html", contexto)


#################################################################


class ListaJuego(ListView):
    
    model= Juego


class DetalleJuego(DetailView):

    model= Juego

class CrearJuego(CreateView):

    model= Juego
    sucess_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion", "genero", "año_de_salida", "tipo_de_juego"]

      
class ActualizarJuego(UpdateView):

    model= Juego
    sucess_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion", "genero", "año_de_salida", "tipo_de_juego"]


class EliminarJuego(DeleteView):

    model= Juego
    sucess_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion"]

