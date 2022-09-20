from django.urls import path
from . import views


urlpatterns = [
    path('', views.getApuntes, name='apuntes'),
    path('apuntes/<int:pk>', views.getApunte, name='apunte'),
    path('apuntes/categorias/<int:pk>', views.getCategoria, name='categoria'),
    path('apuntes/categorias/', views.getCategorias, name='categorias'),
    path('apuntes/add/', views.CreateApunte, name='create-apunte'),
    path('apuntes/update/<int:pk>', views.UpdateApunte, name='update-apunte'),
    path('apuntes/delete/<int:pk>', views.DeleteApunte, name='delete-apunte')
]
