from django.shortcuts import render
from rest_framework import viewsets
from main import models
from main import serializers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
