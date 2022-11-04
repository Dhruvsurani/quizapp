from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, DetailView
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Quiz
from .serializers import CategorySerializer, QuizSerializer


# Create your views here.

class HomeView(TemplateView):
    template_name = 'quiz/home.html'


class ListCategories(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GetQuizes(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class ListQuizes(APIView):
    authentication_classes = []  # disables authentication
    permission_classes = []  # disables permission
    def get(self, request, id=None):
        try:
            quizes = Quiz.objects.filter(category__id=id)
        except Quiz.DoesNotExist:
            raise Http404
        serializer = QuizSerializer(quizes, many=True)
        # quizes = Quiz.objects.all()
        # serializer = QuizSerializer(quizes, many=True)
        return Response(serializer.data)


class StartQuiz(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuizSerializer

    def get_queryset(self):
        cat_id = self.kwargs['category_id']
        return Quiz.objects.filter(category_id=cat_id)
    # q = Quiz.objects.all()
    # queryset = q
    # # breakpoint()
    # print(queryset)
    # def get(self, request, category_id=None):
    #     try:
    #         quiz = Quiz.objects.filter(category_id=category_id)
    #         print(quiz)
    #     except Quiz.DoesNotExist:
    #         raise Http404
    #     serializer = QuizSerializer(quiz, many=True)
    #     return Response(serializer.data)


class AddCategories(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



