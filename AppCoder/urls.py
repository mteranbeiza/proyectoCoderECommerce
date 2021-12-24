from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
  
    path('productos_formulario', views.productos_formulario, name= 'Productos_Formulario'),   
    path('suscriptores_formulario', views.suscriptores_formulario, name= 'Suscriptores_Formulario'),
    path('puntosdeventa', views.puntosdeventa, name= 'PuntosDeVenta'),
    path('puntosdeventa_formulario', views.puntosdeventa_formulario, name= 'Puntosdeventa_Formulario'),
    path('productos', views.ProductosList.as_view(), name= 'Productos'),
]