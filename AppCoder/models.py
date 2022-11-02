from pickle import FALSE, TRUE

from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    documento= models.IntegerField()
    email= models.EmailField(max_length=254, null= TRUE )
    direccion= models.CharField(max_length=60)
    telefono= models.IntegerField()
    pais= models.CharField(max_length=60)
    provincia= models.CharField(max_length=30)
    localidad= models.CharField(max_length=30)

class Juego(models.Model):

    def __str__(self) :
        return f"{self.titulo}"

    titulo= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=70)
    genero= models.CharField(max_length=30)
    año_de_salida= models.IntegerField()
    tipo_de_juego= models.CharField(max_length=60)
    
