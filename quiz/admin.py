from django.contrib import admin
from .models import Question, QuestionChoice, UserAttempts

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'correct_answers']

@admin.register(QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice']

@admin.register(UserAttempts)
class UserAttemptsAdmin(admin.ModelAdmin):
    list_display = ['user', 'Correct_Count', 'Incorrect_Count']