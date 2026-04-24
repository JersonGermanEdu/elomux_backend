from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('listar', views.listar),
    path('crear', views.crear),
    path('actualizar', views.actualizar),
    path('eliminar', views.eliminar),

]