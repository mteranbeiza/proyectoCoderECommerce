from django.db import models

# Create your models here.

class Producto(models.Model):    
    nombre    = models.CharField(max_length=40)
    precio    = models.FloatField()
    categoria = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} Email: {self.mail}  Categoria: {self.categoria}"

   
class Suscriptor(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.EmailField(max_length=140)  

    def __str__(self):
        return f"Nombre: {self.nombre} Email: {self.mail}"
   
    


class PuntoDeVenta(models.Model):
    sucursal = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    calle = models.IntegerField()

    def __str__(self):
        return f"Sucursal: {self.sucursal} Calle: {self.calle} Numero: {self.calle}"

