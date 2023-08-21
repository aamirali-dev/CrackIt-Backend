from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .models import Question, QuestionCategory
from .serializers import QuestionSerializer, QuestionCategorySerializer

@api_view()
def questions(request, category):
    cat = QuestionCategory.objects.get(name=category)
    qas = Question.objects.all().filter(category=cat).prefetch_related('answers')
    serializer = QuestionSerializer(qas, many=True)
    return Response(serializer.data)

@api_view()
def categories(request):
    qc = QuestionCategory.objects.all()
    serializer = QuestionCategorySerializer(qc, many=True)
    return Response(serializer.data)
