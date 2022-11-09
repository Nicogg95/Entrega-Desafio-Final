from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Juego
    
class Juegosingreso(forms.ModelForm):

    class Meta:
        
        model= Juego
        fields=  ["titulo", "descripcion", "genero", "fecha_de_estreno", "tipo_de_juego", "caratula"]

        
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
