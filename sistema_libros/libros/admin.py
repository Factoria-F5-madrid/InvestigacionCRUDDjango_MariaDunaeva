from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('fecha_publicacion',)

admin.site.site_header = "Gestión de la página web"
admin.site.site_title = "Panel de administración"
admin.site.index_title = "Bienvenido al panel de gestión"