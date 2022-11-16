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
from .serializers import (MyTokenObtainPairSerializer,
                          QuestionChoiceSerializer, QuestionSerializer,
                          UserAttemptsSerializer,
                          UserSerializer, )
from rest_framework import  status
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

  

class HomeView(TemplateView):
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
        print(request.user.id)
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



class LoginTemplateView(TemplateView):
    template_name = 'users/login.html'

class MyObtainTokenPairView(TokenObtainPairView, APIView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer