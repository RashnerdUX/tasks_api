from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer, UserSerializer, APIUserSerializer, APITodoSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerReadOnly

# Create your views here.
#This is the Get and Post view for Todos
class ToDoListView(generics.ListCreateAPIView):
    queryset= Todo.objects.all()
    serializer_class = APITodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#This is the view for the Users
class OwnerListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = APIUserSerializer

class SingleOwnerView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = APIUserSerializer

