from django.urls import path
from . import views


urlpatterns = [
    path('', views.Apuntes, name='apuntes'),
    path('apuntes/<str:pk>', views.Apunte, name='apunte'),
    path('apuntes/categorias/<str:pk>', views.Categoria, name='categoria'),
    path('apuntes/categorias/', views.Categorias, name='categorias')
]
