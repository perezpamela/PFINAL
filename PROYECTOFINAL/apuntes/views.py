from django.shortcuts import render, HttpResponse
from .models import Apunte, Categoria, Mensaje, Like

# Create your views here.
def getApuntes(request):
    apuntes = Apunte.objects.all()
    context = {'apuntes':apuntes}
    return render(request, 'apuntes/apuntes.html', context)

def getApunte(request, pk):
    apunte = Apunte.object.get(id=pk)
    context = {'apunte':apunte}
    return render(request, 'apuntes/apunte.html', context)

def getCategorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias':categorias}
    return render(request, 'apuntes/categorias.html', context)

def getCategoria(request, pk):
    categoria = Categoria.objects.get(id=pk)
    context = {'categoria':categoria}
    return render(request, 'apuntes/categoria.html', context)