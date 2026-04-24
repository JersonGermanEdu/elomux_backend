from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

usuarios = [
    {
        "id": 1,
        "nombre": "Juan",
        "email": "juan@example.com"
    },
    {
        "id": 2,
        "nombre": "Maria",
        "email": "maria@example.com"
    }
]


def index(request):
    return HttpResponse("Servidor Basico")

def saludo(request):
    return HttpResponse("Hola Mundo")

def usuario(request):

    if request.method == 'GET':
        return JsonResponse(usuarios, safe=False, json_dumps_params={'indent': 0})
    return HttpResponse("Metodo no permitido")

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        nombre = data.get('nombre')
        email = data.get('email')

        if nombre and email:
            usuarios.append({
                "id": len(usuarios) + 1,
                "nombre": nombre,
                "email": email
            })
            return JsonResponse({"message": "Usuario creado correctamente"}, status=201)
        return JsonResponse({"message": "Nombre y email son requeridos"}, status=400)
    return HttpResponse("Metodo no permitido")