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


#VISTAS EN FUNCIONES

#Vista para registrarse 1
def registro(request):

    if request.method == "POST":

        form = RegistroUsuario(request.POST)

        if form.is_valid():

            username= form.cleaned_data["username"]

            form.save()
            
            return render (request,"AppCoder/Usuarios/resultadoregistro.html", {"mensaje": "Usuario creado."}) 

    else: 

        form = RegistroUsuario()

    return render (request,"AppCoder/Usuarios/registro.html", {"formulario":form})


#################################################################

#Vista para mostrarel resultado del registro
def resultadoregistro(request):

    return render (request,"AppCoder/Usuarios/resultado.html")


#################################################################

#Vista para iniciar sesion
def inicioSesion(request):

    if request.method=="POST":

        form= AuthenticationForm(request, data= request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password= contraseña)

            if user:

                login(request,user)

                return render (request,"AppCoder/inicio.html", {"usuario": user})
            
        else:
            
            form = AuthenticationForm()
            return render (request,"AppCoder/Usuarios/login.html", {"mensaje": "Datos incorrectos. Intente nuevamente.", "formulario": form}) 

    else:

        form = AuthenticationForm()

    return render (request,"AppCoder/Usuarios/login.html", {"formulario": form})


#################################################################

#Vista de la ventana principal
@login_required
def inicio(request):

    return render (request,"AppCoder/inicio.html")


#################################################################

#Vista con informacion
def about(request):

    return render (request,"AppCoder/about.html")


#################################################################
    
#Vista para editar usuario
@login_required
def editarUsuario(request):

    usuario= request.user

    if request.method == "POST":

        form= FormularioEditar(request.POST)
    
        if form.is_valid():

            info = form.cleaned_data

            usuario.email= info ["email"]
            usuario.set_password (info["password1"])
            usuario.first_name= info ["first_name"]
            usuario.last_name= info ["last_name"]

            usuario.save()


        return render (request, "AppCoder/inicio.html")
        
    else: 
        
        form= FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name, 
            "last_name": usuario.last_name,})
        
        contexto=  {"formulario": form, "usuario": usuario}

    return render (request, "AppCoder/Usuarios/editarUsuario.html", contexto)


#################################################################

#Vista para buscar un juego 1
@login_required
def buscar(request):

    return render (request,"AppCoder/Juegos/buscar.html")


#################################################################

#Vista para buscar un juego 2
def busquedajuego(request):


    if "tit" in request.GET:

        titulo = request.GET["tit"]

    else:

        titulo = False


    if titulo:
     
        titulo= Juego.objects.filter(titulo__icontains=titulo)

        return render (request,"AppCoder/Juegos/busquedaJuego.html", {"titulo": titulo})

    else:

        return render(request, "AppCoder/Juegos/busquedaJuego.html")

    
#################################################################


#VISTAS EN CLASES


class ListaJuego(LoginRequiredMixin, ListView):
    
    model= Juego  


class DetalleJuego(LoginRequiredMixin, DetailView):

    model= Juego

    
class CrearJuego(LoginRequiredMixin, CreateView):

    model= Juego
    success_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion", "genero", "fecha_de_estreno", "tipo_de_juego", "caratula"]

      
class ActualizarJuego(LoginRequiredMixin, UpdateView):

    model= Juego
    success_url = "/AppCoder/juego/list"
    fields = ["titulo", "descripcion", "genero", "fecha_de_estreno", "tipo_de_juego", "caratula"]


class EliminarJuego(LoginRequiredMixin, DeleteView):

    model= Juego
    success_url = "/AppCoder/juego/list"

