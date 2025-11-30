from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TareaForm
from .models import Tarea

#Vista pública con video demo
def demo_video(request):
    return render(request, 'tareas/demo_video.html')

#Registro
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('lista_tareas')
    return render(request, 'registration/register.html', {'form': form})

#Lista de tareas (privada)
@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas/lista.html', {'tareas': tareas})

#Detalle
@login_required
def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    return render(request, 'tareas/detalle.html', {'tarea': tarea})

#Agregar
@login_required
def agregar_tarea(request):
    form = TareaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        Tarea.objects.create(
            titulo=form.cleaned_data['titulo'],
            descripcion=form.cleaned_data['descripcion'],
            usuario=request.user
        )
        return redirect('lista_tareas')
    return render(request, 'tareas/agregar.html', {'form': form})

#Eliminar
@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == "POST":
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'tareas/eliminar.html', {'tarea': tarea})
