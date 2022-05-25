**Sprint_M7_grupal**

Grupo 1

El proyecto consta de la creación de un sitio web para la creación de un sitio web para la venta de productos llamando telovendo.
Consta de una landing page de la tienda con su historia, productos, ubicación y contacto.
Cuenta con inicio de sesión, creación de cuenta, y contacto si el usuario no está registrado. Si ha iniciado sesión puede ver el catálogo de productos y acceder a sus mensajes pudiendo editarlos o eliminarlos o enviar uno nuevo.
Si es administrador puede también revisar todos los mensajes que ha recibido, ver las listas de clientes, proveedores, productos, pudiendo agregar nuevos mediante formulario. También se modificó el sitio de admin de django con django interface donde podemos y se puede eliminar o modificar productos y proveedores. Además creamos el modelo de categorias y subcategorias y las relacionamos con proveedores y productos mediante Foreign Key. Y se puede filtrar por categorías los productos en el sitio de admin de django.

Instrucciones instalación:

- Clonar el repositorio https://github.com/LiliGC/AE3_M7_grupal.git
- Crear el entorno virtual
- Instalar el archivo de requirements.txt
- Hacer las migraciones, makemigrations y luego migrate.
- Crear el superusuario o proceder a cargar el archivo de datos que usamos el que nombramos data1.json
- Aplicar el comando migrate.
- Y por ultimo correr el servidor con python manage.py runserver.

## Tecnologías y librerías usadas

Revisar el archivo requirements.txt. Algunas observaciones:

    Se usó la versión más reciente de Django para crear la aplicación.
    Se usó HTML, Bootstrap 5, CSS, JavaScript para crear los templates.
    Para el formulario se usó los que trae django junto con crispy forms para el estilo.
    Para las tablas con el listado de clientes, productos y proveedores se uso DataTable de jquery.
    Para los mensajes de alerta se usó bootstrap
    Se modificó la página del admin importando la librería admin_interface.
    Se usó pillow para la carga de las imágenes de los productos.

### Consideraciones

-Se usaron restricciones en el template base en barra de navegación para dar acceso a los clientes a ciertas páginas y al staff a otras.También en las views le usaron las restricciones @login_required y @staff_required. En el admin de django se establecieron grupos para los permisos siendo estos clientes, administadores. -Se puede observar en la siguiente imagen la vista de la barra de navegación con las opciones si no ha iniciado sesión.

