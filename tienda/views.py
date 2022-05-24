from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProveedorForm, ProductoForm, ContactoForm
from .models import Cliente, Proveedor, Producto, Contacto



# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

@staff_member_required
@login_required
def estadistica(request):
    return render(request, 'tienda/estadistica.html')

@staff_member_required
@login_required
def clientes(request):
    cliente=Cliente.objects.all().values()
    context = {
    'clientes': cliente,
    }
    return render(request, 'tienda/clientes.html', context)

@login_required
def proveedores(request):
    proveedor=Proveedor.objects.all()
    context = {
    'proveedores': proveedor,
    }
    return render(request, 'tienda/proveedores.html', context)

@login_required
def listacontactos(request):
    contacto=Contacto.objects.all()
    context = {
    'contactos': contacto,
    }
    return render(request, 'tienda/listacontactos.html', context)

@login_required
def listadoprod(request):
    producto=Producto.objects.all()
    context = {
    'productos': producto,
    }
    return render(request, 'tienda/listadoprod.html', context)

def catalogoprod(request):
    producto=Producto.objects.all()
    context = {
    'productos': producto,
    }
    return render(request, 'tienda/catalogoprod.html', context)


@staff_member_required
@login_required
def registroprov(request):

    form=ProveedorForm()

    if request.method == 'POST':
		
        form = ProveedorForm(request.POST)

        if form.is_valid():
            proveedor=Proveedor()
            proveedor.nombre=form.cleaned_data["nombre"]
            proveedor.categoria=form.cleaned_data["categoria"]
            proveedor.subcategoria=form.cleaned_data["subcategoria"]
            proveedor.marca=form.cleaned_data["marca"]
            proveedor.telefono=form.cleaned_data["telefono"]
            proveedor.correo_electronico=form.cleaned_data["correo_electronico"]
            proveedor.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente')
        else: messages.error('Inválido')
        return redirect('index')
    else:
        form=ProveedorForm() 
        return render(request, 'tienda/registroprov.html', {"form":form}) 

@staff_member_required
@login_required
def registroprod(request):

    form=ProductoForm()

    if request.method == 'POST':
		
        form = ProductoForm(request.POST, request.files)

        if form.is_valid():
            producto=Producto()
            producto.nombre=form.cleaned_data["nombre"]
            producto.marca=form.cleaned_data["marca"]
            producto.moda=form.cleaned_data["moda"]
            producto.tipo=form.cleaned_data["tipo"]
            producto.precio=form.cleaned_data["precio"]
            producto.stock=form.cleaned_data["stock"]
            producto.color=form.cleaned_data["color"]
            producto.talla=form.cleaned_data["talla"]
            producto.imagen=form.cleaned_data["imagen"]
            producto.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente')
        else: messages.error('Inválido')
        return redirect('index')
    else:
        form=ProductoForm() 
        return render(request, 'tienda/registroprod.html', {"form":form}) 

@login_required
def contacto(request):

    form=ContactoForm()

    if request.method == 'POST':
		
        form = ContactoForm(request.POST)

        if form.is_valid():
            contacto=Contacto()
            contacto.nombre=form.cleaned_data["nombre"]
            contacto.correo_electronico=form.cleaned_data["correo_electronico"]
            contacto.tipo_consulta=form.cleaned_data["tipo_consulta"]
            contacto.mensaje=form.cleaned_data["mensaje"]
            contacto.save()
            messages.success(request, 'Su  mensaje ha sido enviado satisfactoriamente')
        else: messages.error('Inválido')
        return redirect('index')
    else:
        form=ContactoForm() 
        return render(request, 'tienda/contacto.html', {"form":form}) 

@login_required
def mismensajes(request):
    email=request.user.email
    mensaje=Contacto.objects.filter(correo_electronico=email).all()
    context = {
    'mensajes': mensaje,
    }
    return render(request, 'tienda/mismensajes.html', context)


@login_required
def contacto_edit(request,pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()
            messages.success(request, 'Su mensaje se ha modificado con éxito')
            return redirect('listacontactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'tienda/contacto_edit.html', {'form': form})

@login_required
def contacto_delete(request,pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    messages.warning(request, 'Esta seguro que desea eliminar su mensaje?')        
    return redirect('listacontactos')

def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect('index')
		messages.error(request, "Registro no exitoso. Información no válida.")
	form = NewUserForm()
	return render (request, 'tienda/register_user.html', context={"register_form":form})


def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Tu haz iniciado sesión como {username}.")
				return redirect('index')
			else:
				messages.error(request,"Nombre o contraseña no válidos.")
		else:
			messages.error(request,"Nombre o contraseña no válidos.")
	form = AuthenticationForm()
	return render(request, 'tienda/login.html',context={"login_form":form})

@login_required
def logout_user(request):
	logout(request)
	messages.info(request, "Haz cerrado sesión exitosamente.") 
	return redirect('index')
