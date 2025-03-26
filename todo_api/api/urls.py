from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('todolist/', views.ToDoListView.as_view(), name='List of ToDos'),
    path('users/', views.OwnerListView.as_view(), name='List of Users'),
    path('users/<int:pk>', views.SingleOwnerView.as_view(), name='User'),
]