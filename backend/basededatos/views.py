from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario

def index(request):
    return JsonResponse({'mensaje': 'API CRUD PostgreSQL funcionando'})

def listar(request):
    try:
        usuarios = Usuario.objects.all().order_by('id')
        datos = []
        for row in usuarios:
            datos.append({
                'id': row.id,
                'nombre': row.nombre,
                'email': row.email
            })
        return JsonResponse(datos, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def crear(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Método no permitido')
    try:
        body = json.loads(request.body)
        nombre = body.get('nombre')
        email = body.get('email')
        if not nombre or not email:
            return HttpResponseBadRequest('Faltan datos requeridos')
        usuario = Usuario.objects.create(nombre=nombre, email=email)
        return JsonResponse({'mensaje': 'Usuario creado', 'id': usuario.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def actualizar(request):
    if request.method != 'PUT':
        return HttpResponseBadRequest('Método no permitido')
    try:
        body = json.loads(request.body)
        user_id = body.get('id')
        nombre = body.get('nombre')
        email = body.get('email')
        if not user_id or not nombre or not email:
            return HttpResponseBadRequest('Faltan datos requeridos')
        actualizado = Usuario.objects.filter(id=user_id).update(nombre=nombre, email=email)
        if actualizado == 0:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        return JsonResponse({'mensaje': 'Usuario actualizado'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def eliminar(request):
    if request.method != 'DELETE':
        return HttpResponseBadRequest('Método no permitido')
    try:
        body = json.loads(request.body)
        user_id = body.get('id')
        if not user_id:
            return HttpResponseBadRequest('Faltan datos requeridos')
        eliminado = Usuario.objects.filter(id=user_id).delete()[0]
        if eliminado == 0:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        return JsonResponse({'mensaje': 'Usuario eliminado'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)