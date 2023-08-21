from rest_framework import serializers
from .models import QuestionCategory, Question, Solution

class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = ['name']

class SolutionSerializerInline(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['data']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['description', 'answers']
    answers = SolutionSerializerInline(many=True)