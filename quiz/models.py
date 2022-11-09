from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    question_text = models.CharField(max_length=150)
    correct_answers = models.CharField(max_length=60)

    def __str__(self):
        return self.question_text


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = ArrayField(
        models.CharField(max_length=1000, blank=True),
        size=4,
    )

    class Meta:
        verbose_name_plural = 'Quizes'



