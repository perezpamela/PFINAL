from django.contrib import admin
from .models import Apunte, Mensaje, Categoria, Like, CategoriasApuntes

# Register your models here.
admin.site.register(Apunte)
admin.site.register(Mensaje)
admin.site.register(Categoria)
admin.site.register(Like)
admin.site.register(CategoriasApuntes)