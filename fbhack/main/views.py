from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from main import models
from main import serializers

# User.
class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('first_name',)
    filter_fields = ('is_specialist', 'rating', 'skills__tag')

class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

# Skill
class SkillList(generics.ListCreateAPIView):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.UserSerializer

class SkillViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('tag',)
    filter_fields = ('',)


# Question
class QuestionList(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.UserSerializer


class QuestionViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('skills__tag',)

# Chat
class ChatList(generics.ListCreateAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.UserSerializer

class ChatViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)



