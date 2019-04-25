from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def list(request):
#     person = Person.objects.all()
#     return render(request, 'person/person_list.html', {'person':person})
    
# 위 3줄과 완벽히 같은 역할을 하는 클래스
class PersonList(ListView):
    model = Person  # 무슨 모델을 이용할지
    context_object_name = 'person'  # 가져온 정보를 저장할 변수명
    
    
# def create(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person:list')
#     else:
#         form = PersonForm()
#     return render(request, 'person/person_form.html', {'form':form})

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/person/'