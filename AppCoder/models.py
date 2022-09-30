from pickle import FALSE, TRUE
from django.db import models

# Create your models here.

class Clientes(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    documento= models.IntegerField()
    email= models.EmailField(max_length=254, null= TRUE )
    direccion= models.CharField(max_length=60)
    telefono= models.IntegerField()
    pais= models.CharField(max_length=60)
    provincia= models.CharField(max_length=30)
    localidad= models.CharField(max_length=30)
