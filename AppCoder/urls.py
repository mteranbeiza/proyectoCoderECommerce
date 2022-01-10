from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio', views.inicio, name= 'Inicio'),
  
    path('productos_formulario', views.productos_formulario, name= 'Productos_Formulario'),   
    path('productos', views.ProductosList.as_view(), name= 'Productos'),
    
    path('suscriptores_formulario', views.suscriptores_formulario, name= 'Suscriptores_Formulario'),

    path('puntosdeventa', views.puntosdeventa, name= 'PuntosDeVenta'),
    path('puntosdeventa_formulario', views.puntosdeventa_formulario, name= 'Puntosdeventa_Formulario'),
    path('puntosdeventa_list', views.PuntosdeventaList.as_view(), name= " List "),
    path(r'^ (?P<pk>\d+)$', views.PuntosdeventaDetalle.as_view(), name= "Detail"),
    path("leerSuscriptores", views.leerSuscriptores, name="LeerSuscriptores"),
    path("borrarSuscriptores/<suscriptor_nombre>/", views.borrarSuscriptores, name="BorrarSuscriptores"),
    path("editarSuscriptores/<editar_nombre>/", views.editarSuscriptores, name="EditarSuscriptores"),
    path(r'^nuevo$', views.PuntosdeventaCrear.as_view(), name= "Puntosdeventa_Nuevo"),
    path(r'^editar/(?P<pk>\d+)$' , views.PuntosdeventaUpdate.as_view(), name= "Edit"),
    path(r'^borrar/(?P<pk>\d+)$' , views.PuntosdeventaDelete.as_view(), name= "Delete"),
        
      
    path('descripcion/<id>', views.descripcion, name= 'Descripcion'),
    path('login',views.login_request, name="Login"),
    path('register',views.register, name="Register"),
    path('logout',LogoutView.as_view(template_name = 'AppCoder/logout.html'), name='Logout'),
    path('editarPerfil',views.editarPerfil, name="EditarPerfil"),

]