from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Quiz, Answer
from .serializers import CategorySerializer, QuestionSerializer, ChoiceSerializer


# Create your views here.

class HomeView(TemplateView):
    template_name = 'quiz/home.html'


class ListCategories(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class StartQuiz(APIView):

    def get(self, request, category_id=None):
        try:
            quiz = Quiz.objects.get(category__id=category_id)
        except Quiz.DoesNotExist:
            raise Http404
        serializer = QuestionSerializer(quiz.question.all(), many=True)
        return Response(serializer.data)


class AddCategories(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AddAnswers(generics.CreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Answer.objects.all()
