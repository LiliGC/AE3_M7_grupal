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

class Proveedor(models.Model):

    nombre=models.CharField(max_length=50) 

    marca=models.CharField(max_length=50) 

    telefono=models.CharField(max_length=50) 

    correo_electronico=models.EmailField(max_length=50) 

    def __str__(self): 
        return self.marca
        
class Producto(models.Model):
    Polera='polera'
    Poleron= 'poleron'
    Chaqueta='chaqueta'
    Hombre='H'
    Mujer='M'
    Unisex='U'
    Blanco='blanco'
    Negro='negro'
    Gris='gris'
    Small='S'
    Medium='M'
    Large='L'
    XLarge='XL'

    TIPO_CHOICES=[

    (Polera, 'polera'), 

    (Poleron, 'poleron'), 

    (Chaqueta, 'chaqueta'),

    ]

    CATEGORIA_CHOICES=[

    (Hombre, 'Hombre'), 

    (Mujer, 'Mujer'), 

    (Unisex, 'Unisex'),

    ]

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
    tipo_de_producto= models.CharField('tipo de producto',max_length=15,choices=TIPO_CHOICES, default='polera',)
    categoria=models.CharField(max_length=6,choices=CATEGORIA_CHOICES, default='hombre',)
    marca=models.ForeignKey(Proveedor, on_delete=models.PROTECT)
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