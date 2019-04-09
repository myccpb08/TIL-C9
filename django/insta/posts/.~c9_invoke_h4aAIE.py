from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})


def create(request):
    if request.method =='POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():  # 저장해도 되는 값이 들어왔으면
            post_form.save()  # 저장하고
            return redirect('posts:list')   # 리스트페이지를 보여줘
            
        
    else:  # get방식이면
        post_form = PostForm()
        
    return render(request, 'posts/create.html', {'post_form' : post_form})  # 템플릿에서 쓰기 위하여 딕셔너리 key형태로 변수 넘겨줌
    
    
def delete(request, post_id):
    # post = Post.objects.get(pk=post_id)   # 존재하지 않는 key 로 삭제버튼 누르려고 하면, 에러
    post = get_object_or_404(Post, id=post_id)   # 존재하지 않는 key 로 삭제버튼을 누르려고 하면, page not found 페이지 보여줌
    post.delete()
    return redirect('posts:list')
    
def update
    return render(request, 'posts/create.html')