from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class APITodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title =serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=300)
    owner = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class APIUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    todos = APITodoSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance