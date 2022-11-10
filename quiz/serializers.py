from rest_framework import serializers

from .models import Question, QuestionChoice



class QuestionChoiceSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.title')
    class Meta:
        model = QuestionChoice
        fields = ('id','question_id', 'question', 'choice')
        


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'
       
