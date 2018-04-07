from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from main import models
from main import serializers

# Create your views here.
class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('name',)
    filter_fields = ('is_specialist',)


class UserList(generics.ListCreateAPIView):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer