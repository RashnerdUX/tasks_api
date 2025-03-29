from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#This is the model for a To-do list
class Todo(models.Model):
    title = models.TextField(max_length=30, default='Title')
    description = models.TextField(max_length=300)
    #This allows me to designate Todos to the user authorized to create them
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)

    def __str__(self):
        return self.title




