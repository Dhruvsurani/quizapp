from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Question, QuestionChoice, UserAttempts
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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
    fields = ('id', 'user_id', 'Correct_Count', 'Incorrect_Count')

  def create(self, validated_data):
    user=User.objects.filter(id=validated_data['user_id']).first()
    UserAttempts.objects.create(user=user,Correct_Count=validated_data['Correct_Count'],Incorrect_Count=validated_data['Incorrect_Count'])
    return validated_data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token