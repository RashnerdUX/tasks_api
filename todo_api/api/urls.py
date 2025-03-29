from tkinter.font import names

from django.urls import path
from . import views
from rest_framework.authtoken import views as v

urlpatterns = [
    path('todolist/', views.ToDoListView.as_view(), name='List of ToDos'),
    path('todo/<int:pk>/', views.TodoDetail.as_view(), name='Todo Details'),
    path('users/', views.OwnerListView.as_view(), name='List of Users'),
    path('users/<int:pk>/', views.SingleOwnerView.as_view(), name='User'),
    path('api-token-auth/', v.obtain_auth_token),
    path('user/login/', views.LoginView.as_view(), name='User Login'),
    path('user/register/', views.RegisterView.as_view(), name='User Registration'),
    path('chckuser/', views.YourView.as_view(), name='Check Authenticated User'),
]