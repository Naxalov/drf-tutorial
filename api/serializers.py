from .models import Task, User
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(default=False, blank=True, null=True)
    updated = serializers.DateTimeField(auto_now=True)
    created = serializers.DateTimeField(auto_now_add=True)

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    tasks = TaskSerializer(many=True, read_only=True)

