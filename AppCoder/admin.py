from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import *
class ProductoAdmin(admin.ModelAdmin):
    list_display= ("nombre","precio","oferta", "categoria","imagen","foto")
    search_fields = ['nombre']
    list_filter = ['categoria','oferta']
    
    def foto(self,obj):
        return format_html('<img src={} width="100" height="100"/>', obj.imagen.url)

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Suscriptor)
admin.site.register(PuntoDeVenta)