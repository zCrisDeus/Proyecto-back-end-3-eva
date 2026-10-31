from django.contrib import admin
from .models import Tutor, Mascota

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellidos', 'telefono', 'email')
    search_fields = ('rut', 'nombre', 'apellidos', 'email')
    list_filter = ('fecha_registro',)

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'tutor')
    search_fields = ('nombre', 'tutor__nombre', 'tutor__apellidos')
    list_filter = ('especie',)