from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar


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
    descripcion= forms.CharField(max_length=300)
    genero= forms.CharField(max_length=30)
    año_de_salida= forms.IntegerField()
    tipo_de_juego= forms.CharField(max_length=60)

class RegistroUsuario(UserCreationForm):

    email= forms.EmailField()
    password1= forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label= "Repita su contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    
    email= forms.EmailField()
    password1= forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label= "Repita su contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"] 


class AvatarForm(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]