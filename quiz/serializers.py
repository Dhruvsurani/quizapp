from rest_framework import serializers

from .models import Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('__all__',)


class QuizSerializer(serializers.ModelSerializer):
    question_title = serializers.SerializerMethodField()

    def get_question_title(self, obj):
        return obj.question.question_text

    class Meta:
        model = Quiz
        fields = ['category', 'question', 'choice', 'question_title']
        read_only_fields = ('__all__',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('__all__',)


class AnswerSerializer(serializers.ModelSerializer):

    def get_answer(self, obj):
        return obj.question.correct_answers

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('__all__',)
