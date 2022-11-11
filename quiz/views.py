from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, DetailView
from rest_framework import generics, status, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Question, QuestionChoice
from .serializers import QuestionChoiceSerializer, QuestionSerializer, UserSerializer, RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

# Create your views here.

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  

class HomeView(TemplateView):
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

