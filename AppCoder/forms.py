from django import forms 

class Suscriptores_Formulario(forms.Form):
    nombre= forms.CharField()
    mail= forms.CharField()
    telefono= forms.IntegerField() 