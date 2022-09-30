from socket import fromshare
from django import forms

class Clienteregistro(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    documento= forms.IntegerField()
    telefono= forms.IntegerField()
    email= forms.EmailField()
    pais= forms.CharField()
    provincia= forms.CharField()
    localidad= forms.CharField()