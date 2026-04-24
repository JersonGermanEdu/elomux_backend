from django.urls import path
from .views import usuario, index

urlpatterns = [
    path('', index),
    path('usuario/', usuario),
    path('usuario/<int:id>/', usuario),
]