from django.shortcuts import render, redirect
from .models import Post, Comment
# Create your views here.

def new(request):
    return render(request,'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')  # 파일이라서 POST 아님
    
    # DB INSERT
    post = Post(title=title, content=content, image=image)   # new 에서 입력받은 거 받아서 post 에 저장
    post.save()
    
    
    return redirect('posts:detail', post.pk)   # post 요청은 html 모여주는게 아니라 새로운 페이지로 결과를 돌려버림. 그러므로 주소 필요
    

def index(request):
    # All Post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})
    
    
def delete(request, post_id):
    # 삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:list')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post': post})
    
def update(request, post_id):
    # 수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('posts:detail', post.pk)
    

# 댓글 만드는 역할
def comments_create(request, post_id):
    # 댓글을 달 게시물 가져오기
    post = Post.objects.get(pk=post_id)
    
    # detail form 칸에 담겨서 날아온 댓글 내용
    content = request.POST.get('content')
    
    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    
    # 댓글 쓴 글의 디테일 페이지로 가기
    return redirect('posts:detail', post.pk)
    
    
def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    # 삭제한 후, 댓글 썼던 글의 디테일 페이지 보여주기
    return redirect('posts:detail', post_id)