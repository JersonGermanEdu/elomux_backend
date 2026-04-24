from django.urls import path
from .views import saludo, usuario, index, crear_usuario

urlpatterns = [
    path('', index),
    path('saludo/', saludo),
    path('usuario/', usuario),
    path('crear_usuario/', crear_usuario),
]