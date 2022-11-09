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
from .serializers import QuestionChoiceSerializer, QuestionSerializer


# Create your views here.

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

# class ListQuizes(APIView):
#     authentication_classes = []  # disables authentication
#     permission_classes = []  # disables permission
#     def get(self, request, id=None):
#         try:
#             quizes = Quiz.objects.filter(category__id=id)
#         except Quiz.DoesNotExist:
#             raise Http404
#         serializer = QuizSerializer(quizes, many=True)

#         return Response(serializer.data)

# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'


# class StartQuiz(generics.ListAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = QuizSerializer
#     pagination_class = LargeResultsSetPagination

#     def get_queryset(self):
#         cat_id = self.kwargs['category_id']
#         return Quiz.objects.filter(category=cat_id)


# class AddCategories(generics.CreateAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


# class CheckAnswer(generics.ListAPIView):
#     serializer_class = AnswerSerializer
#     permission_classes = (AllowAny, )
#     def get_queryset(self):
#         cat_id = self.kwargs['category_id']
#         return Question.objects.filter(category_id=cat_id)

