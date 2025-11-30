from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_tareas, name='lista_tareas'),
    path('detalle/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),

    # Registro
    path('registrar/', views.register, name='register'),
]