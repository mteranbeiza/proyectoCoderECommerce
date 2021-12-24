from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Producto, Suscriptor, PuntoDeVenta
from AppCoder.forms import Suscriptores_Formulario, Productos_Formulario, Puntosdeventa_Formulario 
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def productos(request):
    return render(request, 'AppCoder/productos.html')

def productos_formulario(request):
    if request.method == "POST":
        productos_formulario= Productos_Formulario(request.POST)
        if productos_formulario.is_valid():
            informacion= productos_formulario.cleaned_data
            producto_instanciado= Producto(nombre= informacion["nombre"],precio= informacion["precio"],categoria=informacion["categoria"])
            producto_instanciado.save()
        return render(request, 'AppCoder/inicio.html')
    
    else:
        productos_formulario= Productos_Formulario
    return render(request, 'AppCoder/productos_formulario.html', {"productos_formulario":productos_formulario})



def suscriptores_formulario(request):
    if request.method == "POST":
        suscriptores_formulario= Suscriptores_Formulario(request.POST)
        if suscriptores_formulario.is_valid():
            informacion= suscriptores_formulario.cleaned_data
            suscriptor_instanciado= Suscriptor(nombre=informacion["nombre"],mail= informacion["email"])
            suscriptor_instanciado.save()
        return render(request, 'AppCoder/inicio.html')
    
    else:
        suscriptores_formulario= Suscriptores_Formulario

    return render(request, 'AppCoder/suscriptores_formulario.html', {"suscriptores_formulario":suscriptores_formulario})


def puntosdeventa(request):
    return render(request, 'AppCoder/puntosdeventa.html')


def puntosdeventa_formulario(request):
    if request.method == "POST":
        puntosdeventa_formulario= Puntosdeventa_Formulario(request.POST)
        if puntosdeventa_formulario.is_valid():
            informacion= puntosdeventa_formulario.cleaned_data
            puntodeventa_instanciado= PuntoDeVenta(nombre=informacion["nombre"],mail= informacion["mail"],barrio= informacion["barrio"])
            puntodeventa_instanciado.save()
        return render(request, 'AppCoder/inicio.html')

    else:
        puntosdeventa_formulario= Puntosdeventa_Formulario

    return render(request, 'AppCoder/puntosdeventa_formulario.html', {"puntosdeventa_formulario":puntosdeventa_formulario})


class ProductosList(ListView):
    model = Producto
    template_name = 'AppCoder/productos.html'    