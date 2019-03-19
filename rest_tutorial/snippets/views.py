from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    """
    REALIZA UNA LISTA DE TODOS LOS SNIPPETS, O CREA UNO NUEVO.
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        datos = JSONParser().parse(request)
        serializer = SnippetSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

def snippet_detail(request, pk):
    """
    Obtiene, actualiza ó elimina un snippet.
    """

    try:
        snippet = Snippet.objects.get(pk = pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        datos = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data = datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)