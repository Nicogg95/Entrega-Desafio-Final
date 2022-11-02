from socket import fromshare

from django import forms


class Usuariosregistro(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    documento= forms.IntegerField()
    telefono= forms.IntegerField()
    email= forms.EmailField()
    pais= forms.CharField()
    provincia= forms.CharField()
    localidad= forms.CharField()

class Juegosingreso(forms.Form):

    titulo= forms.CharField(max_length=30) 
    descripcion= forms.CharField(max_length=70)
    genero= forms.CharField(max_length=30)
    año_de_salida= forms.IntegerField()
    tipo_de_juego= forms.CharField(max_length=60)