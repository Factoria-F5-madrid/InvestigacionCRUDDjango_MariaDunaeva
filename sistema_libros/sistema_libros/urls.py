from django.contrib import admin
from django.urls import path, include
from libros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('libros.urls')),
]

urlpatterns = [
    path('', views.inicio, name='inicio'),  #ruta raíz
    path('admin/', admin.site.urls),
    path('libros/', include('libros.urls')),
]
