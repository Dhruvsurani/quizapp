from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.json import JSONField
User = get_user_model()


class Question(models.Model):
    title = models.CharField(max_length=255)
    correct_answers = models.CharField(max_length=60)
    def __str__(self):
        return self.title


class QuestionChoice(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    choice = ArrayField(
        models.CharField(max_length=1000, blank=True),
        size=4,
    )
    
    def __str__(self):
        return self.question.title


class UserAttempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Completed_Ans = JSONField()
    Correct_Count = models.IntegerField()
    Incorrect_Count = models.IntegerField()
    


