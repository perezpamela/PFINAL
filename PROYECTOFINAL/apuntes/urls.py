from django.urls import path
from . import views


urlpatterns = [
    path('', views.getApuntes, name='apuntes'),
    path('apuntes/<str:pk>', views.getApunte, name='apunte'),
    path('apuntes/categorias/<str:pk>', views.getCategoria, name='categoria'),
    path('apuntes/categorias/', views.getCategorias, name='categorias')
]
