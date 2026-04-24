from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

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
    return HttpResponse("CRUD Basico")

@csrf_exempt
def usuario(request, id=None):
    if request.method == 'GET':
        return JsonResponse(usuarios, safe=False, json_dumps_params={'indent': 0})
    elif request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        email = data.get('email')
        if len(nombre) == 0 or len(email) == 0: 
            return JsonResponse({"message": "ID, o Nombre son requeridos"}, status=400) 

        nuevo_id = usuarios[-1]['id'] + 1 if usuarios else 1
        usuarios.append({
            "id": nuevo_id,
            "nombre": nombre,
            "email": email
        })
        return JsonResponse({"message": "Usuario creado correctamente"}, status=201)
    elif request.method == 'PATCH':
        if id not in [usuario['id'] for usuario in usuarios]:
            return JsonResponse({"message": "Usuario no encontrado"}, status=404)
        data = json.loads(request.body)
        nombre = data.get('nombre')
        email = data.get('email')
        if id and nombre and email:
            usuarios[id - 1] = {
                "id": id,
                "nombre": nombre,
                "email": email
            }
            return JsonResponse({"message": "Usuario actualizado correctamente"}, status=200)
        else:
            return JsonResponse({"message": "ID, nombre y email son requeridos"}, status=400)
    elif request.method == 'DELETE':
        if id not in [usuario['id'] for usuario in usuarios]:
            return JsonResponse({"message": "Usuario no encontrado"}, status=404)

        for index, usuario in enumerate(usuarios):
            if usuario['id'] == id:
                usuarios.pop(index)
                break
        return JsonResponse({"message": "Usuario eliminado correctamente"}, status=200)
    return HttpResponse("Metodo no permitido")