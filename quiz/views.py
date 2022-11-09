from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, DetailView
from rest_framework import generics, status, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Quiz, Question
from .serializers import CategorySerializer, QuizSerializer, AnswerSerializer


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

        return Response(serializer.data)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'


class StartQuiz(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuizSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        cat_id = self.kwargs['category_id']
        return Quiz.objects.filter(category_id=cat_id)


class AddCategories(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CheckAnswer(generics.RetrieveAPIView):
    serializer_class = AnswerSerializer
    permission_classes = (AllowAny, )
    def get_queryset(self):
        ans = self.kwargs['pk']
        return Question.objects.filter(id=ans)

