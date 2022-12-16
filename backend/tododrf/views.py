from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        }
    return Response(api_urls)

# to show all the tasks
@api_view(['GET']) 
def tasklist(request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

# to show a single task
@api_view(['GET'])
def taskdetail(request, pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)

# to create a task
@api_view(['POST'])
def taskcreate(request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# to update a task
@api_view(['POST'])
def taskupdate(request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# to delete a task
@api_view(['DELETE'])
def taskdelete(request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response('Item succsesfully delete!')
        
        


 
# # create a class for the Todo model viewsets
# class taskView(viewsets.ModelViewSet):
 
#     # create a serializer class and
#     # assign it to the TodoSerializer class
#     serializer_class = TaskSerializer
 
#     # define a variable and populate it
#     # with the Todo list objects
#     queryset = Task.objects.all()
