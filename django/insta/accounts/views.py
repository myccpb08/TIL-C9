from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm

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
    

def people(request, username):
    # get_user_model()  #=> User,
    people = get_object_or_404(get_user_model(), username=username)  # 앞의 username=column, 뒤에 username = 주소로부터 넘겨받은
    return render(request, 'accounts/people.html', {'people':people})
    
    
# User Edit(회원정보 수정) - User CRUD 중 U
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user) # 어떤 user 를 수정할건지에 대한 정보 필요
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people', request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request,'accounts/update.html', {'user_change_form': user_change_form}) # 회원정보수정페이지로 연결
    
    
# User Delete(회원탈퇴) - User CRUD 중 D
@login_required
def delete(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')
    

@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save() # 비밀번호 변경되는 순간 = user 인증 만료
            update_session_auth_hash(request, user) # 비밀번호 변경 후, 자동로그인풀림방지
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)  # 어떠한 유저의 비밀번호를 변경할 것인지 인자 필요
    return render(request, 'accounts/password.html', {'password_change_form':password_change_form})