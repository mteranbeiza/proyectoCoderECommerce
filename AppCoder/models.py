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
    nombre = models.CharField(max_length=50, default="", editable=False)
    mail = models.CharField(max_length=40)
    barrio = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} Mail: {self.mail} Barrio: {self.barrio}"

