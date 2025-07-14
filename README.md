# __Investigación y Desarrollo de un CRUD con Django__

## __Parte 1: Aplicación CRUD y Django__



🔄 __¿Qué significa CRUD?__

Un CRUD es un acrónimo que representa las cuatro operaciones básicas que puede realizar una aplicación sobre datos:

C (Create) Crear un nuevo registro en la base de datos; 
R (Read) Leer o visualizar datos existentes; 
U (Update) Modificar un registro existente; 
D (Delete) Eliminar un registro de la base de datos.

🧠 Propósito en aplicaciones web
En el desarrollo web, un CRUD permite a los usuarios gestionar información de forma interactiva. Ya sea en perfiles, productos, publicaciones o comentarios, el CRUD facilita el ciclo completo de vida de los datos. Es la base estructural de la mayoría de sistemas dinámicos, desde redes sociales hasta sistemas administrativos.

🌐 Ejemplo de aplicación web con CRUD

Taskify: Una app de gestión de tareas donde los usuarios pueden:
- 📝 Crear nuevas tareas
- 👁️ Ver la lista de tareas pendientes
- ✏️ Editar detalles como fecha límite o prioridad
- 🗑️ Eliminar tareas completadas o innecesarias
Backend (por ejemplo, en Django o Node.js) se encarga de las operaciones sobre la base de datos, y el frontend (React, Vue, etc.) interactúa mediante formularios y botones que disparan esas acciones.


🔄 __¿Qué son los patrones de arquitectura en desarrollo de software?__

Son esquemas organizativos que definen cómo estructurar y conectar los distintos componentes de una aplicación (datos, lógica, interfaz, etc.). Su objetivo es mejorar la claridad, escalabilidad, mantenibilidad y la separación de responsabilidades.

🎯 ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?
- Modelo: gestiona los datos y la lógica del negocio.
- Vista: se encarga de mostrar los datos al usuario.
- Controlador: recibe las acciones del usuario (como clics o formularios) y coordina entre el modelo y la vista.
💡 Muy usado en frameworks como Ruby on Rails, Laravel o ASP.NET.

🧩 ¿Qué es el patrón MVT (Modelo–Vista–Template)?
Es una variante del MVC adaptada por Django:
- Modelo: define la estructura de los datos (clases en models.py).
- Vista: contiene la lógica que responde a una petición (funciones en views.py).
- Template: archivos HTML que se usan para presentar los datos al usuario.
🎯 La gran diferencia es que Django no tiene un controlador explícito: el enrutador y las vistas hacen esa tarea combinada.

🔍 Diferencias entre MVC y MVT:
- En MVC, el controlador es un componente clave que actúa como intermediario.
- En MVT, Django gestiona el “control” a través del enrutamiento y las funciones de vista, mientras los templates se encargan de la presentación.

🐍 ¿Cuál se usa en Django?
Django utiliza el patrón MVT (Modelo–Vista–Template). Aunque conceptualmente es muy parecido a MVC, Django lo adapta para funcionar con su propio sistema de templates y rutas.


🔄 __¿Cómo se estructura un proyecto en Django? Explicar brevemente el rol de los modelos, vistas, templates y URLs.__

🏗️ Estructura básica de un proyecto en Django
Al crear un proyecto con Django, se genera una carpeta principal que contiene:
  - El archivo manage.py para comandos administrativos
  - Una carpeta del proyecto (por ejemplo miweb/) con la configuración general (settings.py, urls.py, etc.)
  - Una o más aplicaciones (apps) donde se organiza la lógica específica del proyecto

Dentro de cada app, se usan estos cuatro elementos clave:

🔣 Modelos (models.py)
- Definen la estructura de la base de datos usando clases de Python.
- Cada clase representa una tabla, y cada atributo representa una columna.
- También se puede agregar lógica de validación o comportamiento de objetos.

    Ejemplo:
        class Libro(models.Model):
          titulo = models.CharField(max_length=100)
          autor = models.CharField(max_length=100)

👁️ Vistas (views.py)
- Controlan qué sucede cuando el usuario accede a una URL.
- Se encargan de la lógica: recuperar datos, validar formularios, mostrar páginas.

    Ejemplo:
        def lista_libros(request):
            libros = Libro.objects.all()
            return render(request, 'libros.html', {'libros': libros})

🧾 Templates (templates/)
  - Son archivos HTML donde se muestra la información al usuario.
  - Django permite usar variables y lógica básica dentro del HTML usando su lenguaje de plantillas.

🌐 URLs (urls.py)
  - Son el sistema de rutas que conecta URLs con vistas.
  - Permite que el navegador sepa qué función ejecutar cuando alguien accede a una página.
    Ejemplo:
      path('libros/', views.lista_libros, name='libros')

  🔍 ¿Para qué se usa el signo %% en los templates?
      - {% ... %} se usa para estructuras de control: bucles, condiciones, extensiones.
     
     Ejemplo:
        {% for libro in libros %}
          <li>{{ libro.titulo }}</li>
          

🔄 __¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?__

Flujo de datos en Django:
- El usuario rellena y envía el formulario HTML. Esto puede ser un <form> típico con campos como nombre, email, descripción, etc.
- El navegador envía los datos al servidor Django por HTTP POST. Django recibe la solicitud en la vista que corresponde a la URL del formulario.
- La vista procesa los datos. En views.py, normalmente usamos una clase o función que recoge los datos del request.POST.
- El formulario Django valida los datos. En forms.py, puedes definir el formulario con reglas de validación. Django verifica que los datos sean correctos antes de guardarlos.
- Los datos se guardan en el modelo. Si todo es válido, el formulario crea o actualiza una instancia del modelo (que representa una tabla en la base de datos).
- La base de datos registra la nueva información. Se crea un nuevo registro o se modifica uno existente dentro de la base de datos definida en settings.py.
- Django devuelve una respuesta (HTML, redirección, mensaje). Puede mostrar una página de confirmación, volver al formulario, o redirigir a otra vista.
      
      
🔄 __¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD, para qué es cada una? (Por ejemplo: startapp, makemigrations, migrate, runserver, ModelForm, admin, etc.)__

Django viene equipado con una serie de herramientas. Estas son las más utilizadas 👇:

⚙️ startapp
- ¿Para qué sirve?
    Crea una nueva app dentro de tu proyecto Django.
- ¿Por qué es útil para CRUD?
    Es donde definirás tus modelos, vistas, formularios y URLs para gestionar datos.

python manage.py startapp inventario

📦 makemigrations
- ¿Para qué sirve?
    Detecta los cambios en tus modelos y los convierte en archivos de migración.
- ¿Por qué es útil para CRUD?
    Define cómo Django va a crear o modificar las tablas en la base de datos.
  
python manage.py makemigrations

🗄️ migrate
- ¿Para qué sirve?
    Aplica las migraciones a la base de datos, creando las tablas necesarias.
- ¿Por qué es útil para CRUD?
    Es lo que realmente construye la estructura donde se guardan tus datos.
  
python manage.py migrate

🚀 runserver
- ¿Para qué sirve?
    Lanza el servidor de desarrollo local.
- ¿Por qué es útil para CRUD?
    Te permite probar rápidamente tus formularios, vistas y funcionalidad web.
  
python manage.py runserver

📝 ModelForm
- ¿Para qué sirve?
    Crea formularios HTML basados en tus modelos automáticamente.
- ¿Por qué es útil para CRUD?
    Ahorra tiempo y código: puedes crear o editar registros sin escribir el formulario manualmente.

from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']

🛠️ admin
- ¿Para qué sirve?
    Interfaz de administración automática que viene con Django.
- ¿Por qué es útil para CRUD?
    Ya tienes un panel completo para agregar, editar o eliminar registros sin escribir ni una línea extra.

from django.contrib import admin
from .models import Producto

admin.site.register(Producto)


🔄 __¿Cómo funciona el Admin de Django?__

🛠️ El Admin de Django es una interfaz web automática que Django crea para administrar tu base de datos de forma sencilla, sin necesidad de programar formularios ni vistas.

🎯 ¿Qué hace exactamente?
- Muestra una página segura donde puedes crear, editar, eliminar y consultar registros de tus modelos.
- Se genera dinámicamente al registrar tus modelos en admin.py.
- Puedes personalizarlo para mostrar columnas específicas, filtros, búsqueda, validaciones y relaciones entre modelos.

🔑 ¿Cómo se activa?
- Se crea un superusuario (admin)
  
python manage.py createsuperuser

- Ingresa usuario, email y contraseña.

- Registra tus modelos en admin.py
  
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)

- Entra al panel Inicia el servidor con runserver y entra en:
  
http://localhost:8000/admin

💡 ¿Por qué es útil para desarrollo de CRUD?
  - Ahorra tiempo: no necesitas crear formularios ni vistas manuales.
  - Es ideal para administradores y pruebas de datos.
  - Facilita la validación visual de modelos en desarrollo.



