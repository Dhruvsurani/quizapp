from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path("get-details",views.UserDetailAPI.as_view()),
    # path('register',views.RegisterUserAPIView.as_view()),
    path('', views.HomeView.as_view(), name='home'),
    path('questions', views.GetQuestions.as_view()),
    path('questionschoices', views.QuestionChoies.as_view())
]
