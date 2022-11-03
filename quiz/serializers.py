from rest_framework import serializers

from .models import Answer, Category, Question, Quiz



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('__all__',)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('__all__', )


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text')


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    def get_choices(self, obj):
        ordered_queryset = Answer.objects.filter(choices__id=obj.id)
        return ChoiceSerializer(ordered_queryset, many=True, context=self.context).data

    class Meta:
        model = Question
        fields = ('question_text', 'choices')
