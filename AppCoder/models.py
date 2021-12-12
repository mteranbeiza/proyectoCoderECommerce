from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField()
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()

    def __str__(self):
        return f"IdProducto: {self.idProducto} Nombre: {self.nombre} Precio: {self.precio}"

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} Mail: {self.mail} Telefono: {self.telefono}"


class PuntoDeVenta(models.Model):
    sucursal = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    calle = models.IntegerField()

    def __str__(self):
        return f"Sucursal: {self.sucursal} Calle: {self.calle} Numero: {self.calle}"

