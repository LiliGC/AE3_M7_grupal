from django.contrib import admin
from .models import Cliente
from .models import Proveedor
from .models import Producto
from .models import Contacto
from .models import Categoria, Subcategoria
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre', 'marca', 'moda','tipo','precio', 'stock']
    list_editable=['precio', 'stock']
    search_fields=['nombre']
    list_filter=['marca','moda','tipo',]

class ProveedorAdmin(admin.ModelAdmin):
    list_display=['nombre', 'marca', 'categoria','subcategoria']
    search_fields=['nombre']
    list_filter=['marca','categoria','subcategoria',]

admin.site.register(Cliente)

admin.site.register(Proveedor, ProveedorAdmin)

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Contacto)

admin.site.register(Categoria)
admin.site.register(Subcategoria)

