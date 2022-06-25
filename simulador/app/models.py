from pyexpat import model
from django.db import models

# Create your models here.

class PruebaUser(models.Model):
    usuario_pruebas = models.CharField(max_length=30,verbose_name="Usuario Pruebas")
    nombre_pruebas = models.CharField(max_length=30,verbose_name="Usuario Pruebas")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Usuario Prueba'
        verbose_name_plural = 'Usuarios Pruebas'

    def __str__(self):
        return f'Usuario {self.nombre_pruebas}'