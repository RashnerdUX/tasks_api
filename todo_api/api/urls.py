from django.urls import path
from . import views

urlpatterns = [
    path('todolist/', views.ToDoListView.as_view(), name='List of ToDos'),
]