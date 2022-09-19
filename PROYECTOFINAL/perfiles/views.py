from django.shortcuts import render

# Create your views here.
def Perfiles(request):
    context = {}
    return render(request, 'perfiles/perfiles.html', context)

def Perfil(request, pk):
    context = {}
    return render(request, 'perfiles/perfil.html', context)