from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Question, QuestionChoice, UserAttempts


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )

  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])

  password2 = serializers.CharField(write_only=True, required=True)
  
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


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