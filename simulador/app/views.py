from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect


from .forms import *
from .models import *

def index(request):
    return render(request, 'app/index.html')

# Create your views here.
def prueba_usuarios(request):
    context_instance= Requestontext(request)
    
    if request.method=='POST':
        usuario_pruebas = PruebaUser(usuario_pruebas=request.user)
        form = UsuarioPruebaForm(request.POST, instance=usuario_pruebas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('app/index')
        else:
            form=UsuarioPruebaForm
        context =  {'form':form}
        return render ('app/usuariopruebas.html',context, context_instance)