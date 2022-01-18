from django.db import models


# Create your models here.
class Producto(models.Model):
    
    producto = models.CharField('producto', max_length=50)
    tipo = models.CharField('tipo', max_length=50)
    cantidad= models.IntegerField()
    # idCompra= random

class datosPersona(models.Model):
    
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    email = models.EmailField('email' , max_length=254)


class Direccion(models.Model):

    calle = models.CharField('calle', max_length=50)
    altura = models.CharField('altura', max_length=50)
    localidad = models.CharField('localidad', max_length=50)    