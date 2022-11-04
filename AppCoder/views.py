from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


#VISTAS 

def inicioSesion(request):

    if request.method=="POST":

        form= AuthenticationForm(request, data= request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password= contraseña)

            if user:

                login(request,user)

                return render (request,"AppCoder/inicio.html", {"mensaje": f"Bienvenido {user}"})
            
        else:
            
            form = AuthenticationForm()
            return render (request,"AppCoder/login.html", {"mensaje": "Datos incorrectos. Intente nuevamente.", "formulario": form}) 

    else:

        form = AuthenticationForm()

    return render (request,"AppCoder/login.html", {"formulario": form})


#################################################################

"""@login_required
def agregarAvatar (request):
    
    if request.method== "POST":

        form1 = AvatarForm(request.POST, request.FILES)

        if form1.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form1.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form1 = AvatarForm()

    return render(request, "AppCoder/editarUsuario.html", {"formulario1":form1})"""


#################################################################


def registro(request):

    if request.method == "POST":

        form = RegistroUsuario(request.POST)

        if form.is_valid():

            username= form.cleaned_data["username"]

            form.save()
            
            return render (request,"AppCoder/inicio.html", {"mensaje": "Usuario creado."}) 

    else: 

        form = RegistroUsuario()

    return render (request,"AppCoder/registro.html", {"formulario":form})


#################################################################

@login_required
def inicio(request):

    return render (request,"AppCoder/inicio.html")


#################################################################


def about(request):

    return render (request,"AppCoder/about.html")


#################################################################

@login_required
def usuario(request):

    return render (request,"AppCoder/usuario.html")


#################################################################


def resultado(request):

    return render (request,"AppCoder/resultado.html")


#################################################################

@login_required
def buscar(request):

    return render (request,"AppCoder/buscar.html")


#################################################################


def busquedajuego(request):


    if "tit" in request.GET:

        titulo = request.GET["tit"]

    else:

        titulo = False


    if titulo:
     
        titulo= Juego.objects.filter(titulo__iexact=titulo)
        #año_de_salida= Juego.objects.filter(titulo__iexact=titulo)
        #genero= Juego.objects.filter(titulo__iexact=titulo)

        return render (request,"AppCoder/busquedaJuego.html", {"titulos": titulo})

    else:

        return render(request, "AppCoder/busquedaJuego.html")

    
#################################################################
    
@login_required
def editarUsuario(request):

    usuario= request.user

    if request.method == "POST":

        form= FormularioEditar(request.POST)
        form1 = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and form1.is_valid():

            info = form.cleaned_data

            usuario.email= info ["email"]
            usuario.set_password(info["password1"])
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]

            usuario.save()

            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form1.cleaned_data["imagen"])
            avatar.save()

        return render (request, "AppCoder/inicio.html")
        
    else: 
        
        form= FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name, 
            "last_name": usuario.last_name,})
        
        form1 = AvatarForm()
    
        contexto=  {"formulario": form, "formulario1":form1, "usuario": usuario}

    return render (request, "AppCoder/editarUsuario.html", contexto)

#################################################################

"""
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
"""
    
#################################################################
    

def catalogo(request):

    juegos= Juego.objects.all()

    contexto= {"juegos": juegos}

    return render(request, "AppCoder/catalogo.html", contexto)


#################################################################

@login_required
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
    
@login_required
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
        
@login_required
def eliminarJuego(request, tituloJuego):

    juego= Juego.objects.get(titulo=tituloJuego)
    juego.delete()

    juego= Juego.objects.all()

    contexto={"game":juego}

    return render(request,"AppCoder/catalogo.html", contexto)


#################################################################


#VISTAS EN CLASES


class ListaJuego(LoginRequiredMixin, ListView):
    
    model= Juego


class DetalleJuego(LoginRequiredMixin, DetailView):

    model= Juego

    
class CrearJuego(LoginRequiredMixin, CreateView):

    model= Juego
    success_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion", "genero", "año_de_salida", "tipo_de_juego"]

      
class ActualizarJuego(LoginRequiredMixin, UpdateView):

    model= Juego
    success_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion", "genero", "año_de_salida", "tipo_de_juego"]


class EliminarJuego(LoginRequiredMixin, DeleteView):

    model= Juego
    success_url = "/AppCoder/juego/list"

