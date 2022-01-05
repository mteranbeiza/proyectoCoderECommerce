from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
  
    path('productos_formulario', views.productos_formulario, name= 'Productos_Formulario'),   
    path('productos', views.ProductosList.as_view(), name= 'Productos'),
    
    path('suscriptores_formulario', views.suscriptores_formulario, name= 'Suscriptores_Formulario'),

    path('puntosdeventa', views.puntosdeventa, name= 'PuntosDeVenta'),
    path('puntosdeventa_formulario', views.puntosdeventa_formulario, name= 'Puntosdeventa_Formulario'),
    path('puntosdeventa_list', views.PuntosdeventaList.as_view(), name= " List "),
    path(r'^ (?P<pk>\d+)$', views.PuntosdeventaDetalle.as_view(), name= "Detail"),
    path(r'^nuevo$', views.PuntosdeventaCrear.as_view(), name= "Puntosdeventa_Nuevo"),
    path(r'^editar/(?P<pk>\d+)$' , views.PuntosdeventaUpdate.as_view(), name= "Edit"),
    path(r'^borrar/(?P<pk>\d+)$' , views.PuntosdeventaDelete.as_view(), name= "Delete"),
        
      
    path('descripcion/<id>', views.descripcion, name= 'Descripcion'),
]