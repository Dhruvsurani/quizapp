from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, QuestionChoice, UserAttempts
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class QuestionChoiceSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.title')
    class Meta:
        model = QuestionChoice
        fields = ('id','question_id', 'question', 'choice')
        


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'
       

class UserAttemptsSerializer(serializers.ModelSerializer):
  user_id = serializers.IntegerField()
  class Meta:
    model = UserAttempts
    fields = ('id', 'user_id', 'Completed_Ans', 'Correct_Count', 'Incorrect_Count')

  def create(self, validated_data):
    user=User.objects.filter(id=validated_data['user_id']).first()
    UserAttempts.objects.create(user=user,Completed_Ans=validated_data['Completed_Ans'], Correct_Count=validated_data['Correct_Count'],Incorrect_Count=validated_data['Incorrect_Count'])
    return validated_data

