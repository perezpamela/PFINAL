from django.shortcuts import render, HttpResponse

# Create your views here.
def Apuntes(request):
    context = {}
    return render(request, 'apuntes/apuntes.html', context)

def Apunte(request, pk):
    context = {}
    return render(request, 'apuntes/apunte.html', context)

def Categorias(request):
    context = {}
    return render(request, 'apuntes/categorias.html', context)

def Categoria(request, pk):
    context = {}
    return render(request, 'apuntes/categoria.html', context)