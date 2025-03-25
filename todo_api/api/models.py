from django.db import models

# Create your models here.
#This is the model for a To-do list
class Todo(models.Model):
    title = models.CharField(max_length=30),
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

#This is the model for the User
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.SlugField()

    def __str__(self):
        return self.name



