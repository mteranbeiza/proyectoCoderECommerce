from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('productos', views.productos, name= 'Productos'),
    path('productos_formulario', views.productos_formulario, name= 'Productos_Formulario'),
    path('suscriptores', views.suscriptores, name= 'Suscriptores'),
    path('suscriptores_formulario', views.suscriptores_formulario, name= 'Suscriptores_Formulario'),
    path('puntosdeventa', views.puntosdeventa, name= 'PuntosDeVenta'),
]