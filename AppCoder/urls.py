from django.urls import path
from AppCoder import views
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from .urls import *

urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("usuario/", views.usuario,name = "usuario"),
    path("registro/", views.registro, name= "registro"),
    path("resultadoregistro/", views.resultadoregistro, name= "resultadoregistro"),
    path("buscar/", views.buscar, name = "buscar"),
    path("busquedaJuego/", views.busquedajuego, name= "BusquedaJuego"),
    path("about/", views.about, name = "about"),
    path("login/", views.inicioSesion, name = "login"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/Usuarios/logout.html"), name= "logout"),
    path("editarUsuario/", views.editarUsuario, name = "EditarUsuario"),

    #CRUD
    #path("catalogo/", views.catalogo, name = "catalogo"),
    #path("juegoIngreso/", views.juegoIngreso, name= "juegoIngreso"),
    #path("actualizarJuego/<tituloJuego>",views.actualizarJuego, name= "actualizarJuego"),
    #path("eliminarJuego/<tituloJuego>",views.eliminarJuego, name= "eliminarJuego"),

  
    #CRUD Clases

    path("juego/list/", views.ListaJuego.as_view(), name="ListaJuego"),
    path("juego/crear/", views.CrearJuego.as_view(), name="CrearJuego"),
    path("juego/<int:pk>", views.DetalleJuego.as_view(), name="DetalleJuego"),
    path("juego/actualizar/<int:pk>", views.ActualizarJuego.as_view(), name="ActualizarJuego"),
    path("juego/eliminar<int:pk>", views.EliminarJuego.as_view(), name="EliminarJuego"),
    
] 

