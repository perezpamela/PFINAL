from django.shortcuts import render, HttpResponse, redirect
from .models import Apunte, Categoria, Mensaje, Like
from .forms import ApunteForm

# Create your views here.
def getApuntes(request):
    apuntes = Apunte.objects.all()
    context = {'apuntes':apuntes}
    return render(request, 'apuntes/apuntes.html', context)

def getApunte(request, pk):
    apunte = Apunte.objects.get(pk=pk)
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

def CreateApunte(request): 
    form = ApunteForm()
    if request.method == 'POST':
        form = ApunteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,'apuntes/apunteForm.html', context)

def UpdateApunte(request,pk):
    apunte = Apunte.objects.get(id=pk)
    form = ApunteForm(instance=apunte)
    if request.method == 'POST':
        form = ApunteForm(request.POST, instance=apunte)
        if form.is_valid():
            form.save()
            url = f'/apuntes/{apunte.id}'
            return redirect(url)
    context = {'form': form}
    return render(request, 'apuntes/apunteForm.html', context)

def DeleteApunte(request, pk):
    apunte = Apunte.objects.get(id=pk)
    if request.method == 'POST':
        apunte.delete()
        apunte.save()
        return redirect('/')
    return render(request, 'apuntes/delete.html', {'obj':apunte})