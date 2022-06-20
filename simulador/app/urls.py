from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('app/usuariopruebas/', prueba_usuarios, name='usuariopruebas'),
]