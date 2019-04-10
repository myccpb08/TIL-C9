from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            
            # 회원가입하면, 바로 로그인 시켜주도록 하기
            user = signup_form.save()
            auth_login(request,user)
            return redirect('posts:list')
        
    else: # get 방식 요청
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})
    
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():   # 실제 존재하는 user 인지 확인
            auth_login(request, login_form.get_user())   # login_form 에 입력된 user 정보를 가져와서 반환해줌
            return redirect(request.GET.get('next') or 'posts:list')  # next 가 있으면 next 가 우선이니까 앞에 적어야 한다
            
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'login_form':login_form})
    
    
# 로그아웃은 따로 보여주는 페이지가 없으니까, redirect 로 끝냄    
def logout(request):
    auth_logout(request)  # request 안에 들어있는 user 정보를 제거해서 로그아웃함
    return redirect('posts:list')