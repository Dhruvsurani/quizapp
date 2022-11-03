from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('quiz_list/<int:pk>', views.GetQuizes.as_view(), name='quiz-detail'),
    path('category/edit', views.AddCategories.as_view()),
    path('answer/edit', views.AddAnswers.as_view()),
    path('list_category', views.ListCategories.as_view()),
    path('start/', views.ListQuizes.as_view()),
    path('start/<int:category_id>/', views.StartQuiz.as_view()),
]
