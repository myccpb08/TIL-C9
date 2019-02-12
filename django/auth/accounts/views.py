from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.

# 회원가입 폼이 있는 페이지 : user 를 create
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
        
    else:
        form = UserCreationForm()
            
    return render(request,'signup.html', {'form': form} )
    
    
    
# 로그인 기능 : session 을 create   / session delete = log out
    # session : 이 페이지에 접근하는 게 누구인지 임시로 저장하고 있는 공간 (ex. 세션이 만료되었습니다)
                # 페이지를 이동해도, session 이 유지되고 있다면, user 는 변하지 않는다 (ex. 페이지 옮겨도 로그인 유지)
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
            
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
    
    
# 로그아웃

def logout(request):
    auth_logout(request)
    return redirect('posts:list')