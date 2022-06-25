
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


from .forms import *
from .models import *

def index(request):
    return render(request, 'app/index.html')

# Create your views here.

    

    

def usuarios(request):
    usuarios_prueba = PruebaUser.objects.all()
    if request.method == 'POST':

        form = UsuarioPruebaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioPruebaForm()
  
    context = {
        'form': form,
        'usuarios_prueba':usuarios_prueba,
        }
    return render(request, 'app/usuariopruebas.html',context)