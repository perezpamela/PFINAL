from django.urls import path
from . import views


urlpatterns = [
    path('', views.Perfiles, name='perfiles'),
    path('<str:pk>', views.Perfil, name='perfil')
]
