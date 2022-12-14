from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.LoginTemplateView.as_view(), name='Logintemplate'),
    path('home', views.HomeView.as_view(), name='home'),
    path('questions', views.GetQuestions.as_view()),
    path('questionschoices', views.QuestionChoies.as_view()),
    path('userattempts', views.UserAttemptsList.as_view()),
    
]
