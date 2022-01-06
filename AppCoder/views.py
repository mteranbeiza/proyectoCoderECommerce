from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Producto, Suscriptor, PuntoDeVenta
from AppCoder.forms import Suscriptores_Formulario, Productos_Formulario, Puntosdeventa_Formulario 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

#PRODUCTOS
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

def descripcion(request,id):
    producto = Producto.objects.get(pk=id)
    return render(request, 'AppCoder/descripcion.html',{'producto':producto})
    
class ProductosList(ListView):
    model = Producto
    template_name = 'AppCoder/productos.html'   
 
#SUSCRIPTORES
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


def leerSuscriptores(request):
    suscriptores = Suscriptor.objects.all()
    dicc=  {"suscriptores":suscriptores}
    return render(request, "Appcoder/leerSuscriptores.html", dicc)

def borrarSuscriptores(request, suscriptor_nombre):

    suscriptorBorrar = Suscriptor.objects.get(nombre= suscriptor_nombre)
    suscriptorBorrar.delete()

    suscriptores= Suscriptor.objects.all()
    return render(request, "AppCoder/leerSuscriptores.html", {"suscriptores":suscriptores} )

def editarSuscriptores(request, editar_nombre):
    suscriptor=Suscriptor.objects.get(nombre=editar_nombre)
    
    
    if request.method == "POST":
        miFormulario=Suscriptores_Formulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
        
            suscriptor.nombre = informacion["nombre"],
            suscriptor.mail= informacion["mail"],
            
            suscriptor.save()           
        
        
        return render(request, 'AppCoder/inicio.html')
    
    else:
        miFormulario= Suscriptores_Formulario(initial={"nombre":suscriptor.nombre, "mail":suscriptor.mail})

    return render(request, 'AppCoder/editarSuscriptores.html', {"miFormulario":miFormulario, "editar_nombre":editar_nombre} )


#PUNTOS DE VENTA
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

    return render(request, 'AppCoder/puntodeventa_form.html', {"puntosdeventa_formulario":puntosdeventa_formulario})

class PuntosdeventaList(ListView):
    model = PuntoDeVenta
    template_name = 'AppCoder/puntosdeventa_list.html'

class PuntosdeventaDetalle(DetailView):
    model = PuntoDeVenta
    template_name = 'AppCoder/puntosdeventa_detalle.html' 

class PuntosdeventaCrear(CreateView):
    model = PuntoDeVenta
    sucess_url= '../puntosdeventa_list'  
    fields= ["nombre", "mail", "barrio"]

class PuntosdeventaUpdate(UpdateView):
    model = PuntoDeVenta
    sucess_url= '../puntosdeventa_list'  
    fields= ["mail", "barrio"]

class PuntosdeventaDelete(DeleteView):
    model = PuntoDeVenta
    sucess_url ='../puntosdeventa_list' 