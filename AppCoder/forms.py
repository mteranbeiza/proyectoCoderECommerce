from django import forms 

class Suscriptores_Formulario(forms.Form):
    nombre= forms.CharField()
    email= forms.EmailField()
   


class Productos_Formulario(forms.Form):
    
    nombre    = forms.CharField()
    precio    = forms.FloatField()
    categoria = forms.CharField()

class Puntosdeventa_Formulario(forms.Form):
    nombre= forms.CharField()
    mail= forms.CharField()
    barrio= forms.CharField()

