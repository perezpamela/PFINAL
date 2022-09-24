from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginPage(request):

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario ingresado no existe.')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('apuntes')
        else:
            messages.error(request, 'Usuario o password incorrecta.')

    context = {}
    return render(request,'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('apuntes')