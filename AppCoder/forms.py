from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
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

class UserRegisterForm(UserCreationForm):
    first_name =forms.CharField(label='Nombre')
    last_name= forms.CharField(label = 'Apellido')
    
    username= forms.CharField(label = 'Usuario')
    email= forms.EmailField(label='Mail')
    password1= forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)

    imagen_avatar = forms.ImageField(required=False)

class Meta:
    model = User
    fields = ['first_name','last_name','username','email','password1','password2','imagen_avatar']
    help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    first_name =forms.CharField(label='Nombre')
    last_name= forms.CharField(label = 'Apellido')
    
    username= forms.CharField(label = 'Usuario')
    email= forms.EmailField(label='Mail')
    password1= forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)

    imagen_avatar = forms.ImageField(required=False)


    