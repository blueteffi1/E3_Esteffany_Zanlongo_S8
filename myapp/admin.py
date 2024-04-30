from django.contrib import admin
from .models import MiUsuario  # Importa tu modelo MiUsuario aquí

# Registra tu modelo MiUsuario en el sitio de administración
admin.site.register(MiUsuario)
