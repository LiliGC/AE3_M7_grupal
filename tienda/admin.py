from django.contrib import admin
from .models import Cliente
from .models import Proveedor
from .models import Producto
from .models import Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre', 'tipo_de_producto', 'categoria', 'marca', 'precio', 'stock']
    list_editable=['precio', 'stock']
    search_fields=['nombre']
    list_filter=['marca', 'tipo_de_producto', 'categoria']


admin.site.register(Cliente)

admin.site.register(Proveedor)

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Contacto)