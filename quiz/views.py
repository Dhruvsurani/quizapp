from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView
from rest_framework import generics, status, views, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            )
from .models import Question, QuestionChoice, UserAttempts
from .serializers import (
                          QuestionChoiceSerializer, QuestionSerializer,
                          UserAttemptsSerializer,
                           )
from rest_framework import  status
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class HomeView(TemplateView):
    
  login_url = '/'
  template_name = 'quiz/home.html'


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'


class GetQuestions(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionChoies(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    pagination_class = LargeResultsSetPagination
    serializer_class = QuestionChoiceSerializer
    queryset = QuestionChoice.objects.all()
    filter_fields = ('id')

class UserAttemptsList(APIView):
    
    def get(self, request, format=None):
        # print(request.user.id)
        userattempts = UserAttempts.objects.filter(user=request.user.id)
        # print(userattempts)
        serializer = UserAttemptsSerializer(userattempts, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = UserAttemptsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginTemplateView(TemplateView):
    template_name = 'users/login.html'

