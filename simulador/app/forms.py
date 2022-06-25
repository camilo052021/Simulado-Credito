from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from. models import *
class UsuarioPruebaForm(ModelForm):

    class Meta:
        model = PruebaUser
        fields = ['usuario_pruebas','nombre_pruebas',]
	