from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('productos', views.productos, name= 'Productos'),
    path('suscriptores', views.suscriptores, name= 'Suscriptores'),
    path('puntosdeventa', views.puntosdeventa, name= 'PuntosDeVenta'),
]