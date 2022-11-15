from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, DetailView
from rest_framework import generics, status, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Question, QuestionChoice, UserAttempts
from .serializers import QuestionChoiceSerializer, QuestionSerializer, UserAttemptsSerializer, UserSerializer, RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  

class HomeView(LoginRequiredMixin, TemplateView):
  login_url = '/'
  template_name = 'quiz/home.html'


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'


class GetQuestions(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionChoies(generics.ListAPIView):
    permission_classes = (AllowAny, )
    pagination_class = LargeResultsSetPagination
    serializer_class = QuestionChoiceSerializer
    queryset = QuestionChoice.objects.all()
    filter_fields = ('id')

class UserAttemptsList(APIView):
    
    def get(self, request, format=None):
        User_attempts = UserAttempts.objects.filter(user=request.user.id)
        print(User_attempts)
        serializer = UserAttemptsSerializer(User_attempts, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = UserAttemptsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)