from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Apunte(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    portada = models.CharField(max_length=200)
    creador = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-last_updated_date', '-created_date']

    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class CategoriasApuntes(models.Model):
    apunte = models.ForeignKey(Apunte, default=1, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, default=1, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'El apunte {self.apunte} se sumó a la categoría {self.categoria}.'

class Mensaje(models.Model):
    usuario = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    apunte = models.ForeignKey(Apunte, default=1, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=200)
    contenido = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'El apunte {self.apunte.titulo} recibió un nuevo comentario.'

class Like(models.Model):
    usuario = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    apunte = models.ForeignKey(Apunte, default=1, on_delete=models.CASCADE)
    liked = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'El apunte {self.apunte.titulo} recibió un nuevo like.'




