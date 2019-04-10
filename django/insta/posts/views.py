from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects.order_by('-id').all()
    return render(request, 'posts/list.html', {'posts':posts})
    

@login_required   # decorator 도 하나의 함수,  decorator 의 parameter 로 아래 create 함수를 넘겨줌, 그러므로 함수 앞에 써야한다
                  # 아래 함수를 실행하기 위해서는, 로그인이 되어 있어야 한다 의미
                  # 로그인 안 된 상태에서, 글쓰기 페이지로 들어가면, 자동으로 login 페이지로 돌림
                  # 넘어간 login 페이지 주소창 끝에는 'next=posts/create' 가 표시되어 있음 ( 이 주소로 시도했다가 튕겼다고 표시)
                  # 로그인 후 next 로 보내려면 코드 추가해 주면 됨 (accounts/views.py 에)
def create(request):
    if request.method =='POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():  # 저장해도 되는 값이 들어왔으면
            post = post_form.save(commit=False)  # 객체를 만들었으나, 아직 DB에 저장은 x (commit=False 덕분에)
            post.user = request.user  # post 라는 객체의 user 칸에  request 의 user 를 가져와서 받아줌
            post.save()  # 저장 = 실제 DB 에 반영
            return redirect('posts:list') 
            
        
    else:  # get방식이면
        post_form = PostForm()
        
    return render(request, 'posts/form.html', {'post_form' : post_form})  # 템플릿에서 쓰기 위하여 딕셔너리 key형태로 변수 넘겨줌
    
    
def delete(request, post_id):
    # post = Post.objects.get(pk=post_id)   # 존재하지 않는 key 로 삭제버튼 누르려고 하면, 에러
    post = get_object_or_404(Post, id=post_id)   # 존재하지 않는 key 로 삭제버튼을 누르려고 하면, page not found 페이지 보여줌
    
    if post.user != request.user:
        return redirect('posts:list')
        
    post.delete()
    return redirect('posts:list')
    
    
    
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':  # 그냥 submit 버튼 눌렀을 때
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
        
    else:  # get요청 = 주소창에 주소 입력했을 때
        post_form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'post_form':post_form})