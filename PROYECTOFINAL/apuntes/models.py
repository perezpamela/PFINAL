from django.db import models

# Create your models here.
class Apunte(models.Model):
    #usuario
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    portada = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Mensaje(models.Model):
    #usuario
    apunte = models.ForeignKey(Apunte, default=0)
    asunto = models.CharField(max_length=200)
    contenido = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'El apunte {self.apunte.titulo} recibió un nuevo comentario.'

class Like(models.Model):
    #usuario
    apunte = models.ForeignKey(Apunte, default=0)
    liked = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'El apunte {self.apunte.titulo} recibió un nuevo like.'


