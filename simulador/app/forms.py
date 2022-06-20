from django.forms import ModelForm
from.models import *
class UsuarioPruebaForm(ModelForm):
	
	class Meta:
		model = PruebaUser
		include = ('usuario_pruebas','nombre_pruebas',)