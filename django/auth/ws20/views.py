from django.shortcuts import render, redirect
from .models import Question, Choice
# Create your views here.
def quest(request):
    question=Question.objects.get(pk=1)
    return render(request,'quest.html', {'question':question})