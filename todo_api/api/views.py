from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class ToDoListView(generics.CreateAPIView):
    queryset= Todo.objects.all()
    serializer_class = TodoSerializer


