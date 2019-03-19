from django.shortcuts import render
from django.http import Http404 #HttpResponse , JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetList(APIView):
    """
    Lista todos los snippets, o crea uno nuevo.
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        datos = JSONParser().parse(request)
        serializer = SnippetSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):

    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk = pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = SnippetSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        datos = self.get_object(pk)
        serializer = SnippetSerializer(datos, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):    
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

"""
Tutorial 2
# Tutorial 1
# @csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
   
    REALIZA UNA LISTA DE TODOS LOS SNIPPETS, O CREA UNO NUEVO.
   
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        datos = JSONParser().parse(request)
        serializer = SnippetSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status = 201)
        # return JsonResponse(serializer.errors, status = 400)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format = None):
    Obtiene, actualiza ó elimina un snippet.
   
    try:
        snippet = Snippet.objects.get(pk = pk)
    except Snippet.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        datos = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data = datos)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status = 400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        # return HttpResponse(status=204)
        return Response(status = status.HTTP_204_NO_CONTENT)
"""