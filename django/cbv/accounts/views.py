from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class Login(LoginView):
    pass

# templates/registration/login.html 이 default 니까 그대로 만들어줌