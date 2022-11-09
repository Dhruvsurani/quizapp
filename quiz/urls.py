from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('questions', views.GetQuestions.as_view()),
    path('questionschoices', views.QuestionChoies.as_view())
]
