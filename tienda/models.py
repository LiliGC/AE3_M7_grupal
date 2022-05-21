from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Categoria(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self): 
        return self.nombre

class Subcategoria(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self): 
        return self.nombre

class Proveedor(models.Model):

    nombre=models.CharField(max_length=50) 

    marca=models.CharField(max_length=50) 

    telefono=models.CharField(max_length=50) 

    correo_electronico=models.EmailField(max_length=50)

    categoria=models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)

    subcategoria=models.ForeignKey(Subcategoria, null=True, on_delete=models.SET_NULL)

    def __str__(self): 
        return self.marca
        
class Producto(models.Model):
    Blanco='blanco'
    Negro='negro'
    Gris='gris'
    Small='S'
    Medium='M'
    Large='L'
    XLarge='XL'

    COLOR_CHOICES=[

    (Blanco, 'blanco'), 

    (Negro, 'negro'), 

    (Gris, 'gris'),

    ]

    TALLA_CHOICES=[

    (Small, 'S'), 

    (Medium, 'M'), 

    (Large, 'L'),

    (XLarge, 'XL'),

    ]

    nombre=models.CharField(max_length=50)
    marca=models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    moda=models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    tipo=models.ForeignKey(Subcategoria, null=True, on_delete=models.SET_NULL)
    precio=models.IntegerField()
    stock=models.IntegerField()
    color=models.CharField(max_length=10,choices=COLOR_CHOICES, default='blanco')
    talla=models.CharField(max_length=2,choices=TALLA_CHOICES, default='small')
    imagen=models.ImageField(upload_to='productos')


    def __str__(self): 
        return self.nombre

consultas=[
    [0, 'consulta'],
    [1, 'reclamo'],
    [2, 'sugerencia'],
    [3, 'felicitaciones']
]
class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=30)
    tipo_consulta=models.IntegerField(choices=consultas)
    mensaje=models.TextField()

    def __str__(self): 
        return self.nombre