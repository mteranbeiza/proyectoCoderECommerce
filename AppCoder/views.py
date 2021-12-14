from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Suscriptor
from AppCoder.forms import Suscriptores_Formulario

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def productos(request):
    return render(request, 'AppCoder/productos.html')

def suscriptores(request):
    return render(request, 'AppCoder/suscriptores.html')

def suscriptores_formulario(request):
    if request.method == "POST":
        suscriptores_formulario= Suscriptores_Formulario(request.POST)
        if suscriptores_formulario.is_valid():
            informacion= suscriptores_formulario.cleaned_data
            suscriptor_instanciado= Suscriptor(nombre=informacion["nombre"],mail= informacion["mail"],telefono= informacion["telefono"])
            suscriptor_instanciado.save()
        return render(request, 'AppCoder/inicio.html')
    
    else:
        suscriptores_formulario= Suscriptores_Formulario

    return render(request, 'AppCoder/suscriptores_formulario.html', {"suscriptores_formulario":suscriptores_formulario})


def puntosdeventa(request):
    return render(request, 'AppCoder/puntosdeventa.html')