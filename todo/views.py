from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

@api_view()
def todo_home(request):
    return Response({'home': 'This is home page'})


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    


#@api_view(['GET', 'DELETE', 'PUT'])
#def todo_detail(request, id):
#    todo = get_object_or_404(Todo,id=id)
#
#    if request.method == 'GET':
#        serializer = TodoSerializer(todo)
#        return Response(serializer.data)
#
#    if request.method == 'PUT':
#        serializer = TodoSerializer(data = request.data, instance=todo)
#        serializer.is_valid()
#        serializer.save()
#        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#    
#    if request.method == 'DELETE':
#        todo.delete()
#        return Response ({'message':'Todo delete succesfully'})
    
@api_view(['GET', 'DELETE', 'PUT'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'todo deleted succesfully'})




class Todos(ListCreateAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer
    lookup_field = 'id'


class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

