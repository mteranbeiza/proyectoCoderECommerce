from django import forms 

class Suscriptores_Formulario(forms.Form):
    nombre= forms.CharField()
    mail= forms.CharField()
    telefono= forms.IntegerField() 


class Productos_Formulario(forms.Form):
    idProducto= forms.IntegerField() 
    nombre= forms.CharField()
    precio= forms.FloatField()