from django.urls import path
from . import views

urlpatterns = [
    path('titulo/',views.titulo),
    path('contenido/',views.contenido),
]