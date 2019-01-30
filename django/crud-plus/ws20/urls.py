from django.urls import path
from . import views

app_name = 'ws20'  



urlpatterns = [
    path('question', views.quest),
]