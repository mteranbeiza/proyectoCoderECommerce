from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio', views.inicio, name= 'Inicio'),
  
    path('productos_formulario', views.productos_formulario, name= 'Productos_Formulario'),   
    path('productos', views.ProductosList.as_view(), name= 'Productos'),
    
    path('suscriptores_formulario', views.suscriptores_formulario, name= 'Suscriptores_Formulario'),
    path("leerSuscriptores", views.leerSuscriptores, name="LeerSuscriptores"),
    path("borrarSuscriptores/<suscriptor_nombre>/", views.borrarSuscriptores, name="BorrarSuscriptores"),
    path("editarSuscriptores/<editar_nombre>/", views.editarSuscriptores, name="EditarSuscriptores"),

    path('puntosdeventa', views.puntosdeventa, name= 'PuntosDeVenta'),
    path('puntosdeventa_formulario', views.puntosdeventa_formulario, name= 'Puntosdeventa_Formulario'),
    path('leer_puntosdeventa', views.leerPuntosdeventa, name='LeerPuntosdeventa'),
    path("borrarPuntosdeventa/<puntodeventa_nombre>/", views.borrarPuntosdeventa, name="BorrarPuntosdeventa"),
    path("editarPuntosdeventa/<editar_nombre>/", views.editarPuntosdeventa, name="EditarPuntosdeventa"), 
  
    path('descripcion/<id>', views.descripcion, name= 'Descripcion'),
    path('login',views.login_request, name="Login"),
    path('register',views.register, name="Register"),
    path('logout',LogoutView.as_view(template_name = 'AppCoder/logout.html'), name='Logout'),
    path('editarPerfil',views.editarPerfil, name="EditarPerfil"),

]