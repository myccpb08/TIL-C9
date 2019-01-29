from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def new(request):
    return render(request,'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB INSERT
    post = Post(title=title, content=content)   # new 에서 입력받은 거 받아서 post 에 저장
    post.save()
    
    
    return redirect(f'/posts/{post.pk}')   # post 요청은 html 모여주는게 아니라 새로운 페이지로 결과를 돌려버림. 그러므로 주소 필요
    

def index(request):
    # All Post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})
    
    
def naver(request, q):  # 외부 페이지로 redirect 시키기
    return redirect(f'https://search.naver.com/search.naver?query={q}')
    
def delete(request, post_id):
    # 삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post': post})
    
def update(request, post_id):
    # 수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect(f'/posts/{post_id}/')
    
    
    