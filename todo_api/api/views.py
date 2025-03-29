from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework import generics, permissions, response, status, authentication
from rest_framework.authtoken.models import Token
from .models import Todo
from .serializers import UserSerializer, TodoSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .permissions import IsOwnerReadOnly
from django.shortcuts import get_object_or_404

# Create your views here.
#This is the Get and Post view for Todos
class ToDoListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        print(f"User authenticated: {request.user.is_authenticated}")
        print(f"User: {request.user}")

        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        print(f"User authenticated: {request.user.is_authenticated}")
        print(f"User: {request.user}")

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):

    #This will query the database for a single item using primary key
    def get_object(self, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            return todo
        except:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serialized = TodoSerializer(instance=todo)
        return response.Response(data=serialized.data, status=200)

    def put(self, request, pk):
        todo = self.get_object(pk=pk)
        serialized = TodoSerializer(todo, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return response.Response(data=serialized.data, status=201)
        return response.Response(data=serialized.errors, status=400)

    def patch(self, request, pk):
        todo = self.get_object(pk=pk)
        serialized = TodoSerializer(todo, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return response.Response(serialized.data, status=200)
        return response.Response(serialized.errors, status=400)

    def delete(self, request, pk):
        todo = self.get_object(pk=pk)
        todo.delete()
        return response.Response(data={"message":f"The item with the id {pk} has been deleted"},status=201)

#This is the view for the Users
class OwnerListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return response.Response(serializer.data)

class SingleOwnerView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return response.Response(serializer.data)

#These are the views for registering and getting users their tokens
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        #This checks that the User is in the database
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return response.Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return response.Response(data=user.data, status=status.HTTP_201_CREATED)
        return response.Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)

#For testing
class YourView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # This method will only be accessible to authenticated users
        return response.Response({"message": "You are authorized"})

