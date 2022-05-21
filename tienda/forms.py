from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.forms import ModelForm
from .models import Proveedor, Producto, Contacto


class ProveedorForm(ModelForm):

    class Meta:
        model=Proveedor
        fields='__all__'
    
    labels = {
        'nombre':  'Nombre de representante',
        'marca': 'Marca',
        'telefono': 'Teléfono de contacto',
        'correo_electronico': 'Email',
    }


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields= '__all__'


class ContactoForm(ModelForm):
    class Meta:
        model=Contacto
        fields=['nombre', 'correo_electronico', 'tipo_consulta', 'mensaje']           

            
    