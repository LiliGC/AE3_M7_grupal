from django.urls import path
from django.contrib import admin  
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('mismensajes/', views.mismensajes, name='mismensajes'),
    path('contacto_edit/<int:pk>/', views.contacto_edit, name='contacto_edit'),
    path('contacto_delete/<int:pk>/', views.contacto_delete, name='contacto_delete'),
    path('estadistica/', views.estadistica, name='estadistica'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('listacontactos/', views.listacontactos, name='listacontactos'),
    path('registroprov/', views.registroprov, name='registroprov'),
    path('registroprod/', views.registroprod, name='registroprod'),
    path('listadoprod/', views.listadoprod, name='listadoprod'),
    path('catalogoprod/', views.catalogoprod, name='catalogoprod'),
    path('register_user/',views.register_user, name='register_user'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),

]