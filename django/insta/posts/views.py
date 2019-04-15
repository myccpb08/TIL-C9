from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm, ImageFormSet
from .models import Post, Comment
from django.db import transaction
# Create your views here.

def list(request):
    posts = Post.objects.order_by('-id').all()
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts':posts, 'comment_form':comment_form})
    

@login_required   # decorator 도 하나의 함수,  decorator 의 parameter 로 아래 create 함수를 넘겨줌, 그러므로 함수 앞에 써야한다
                  # 아래 함수를 실행하기 위해서는, 로그인이 되어 있어야 한다 의미
                  # 로그인 안 된 상태에서, 글쓰기 페이지로 들어가면, 자동으로 login 페이지로 돌림
                  # 넘어간 login 페이지 주소창 끝에는 'next=posts/create' 가 표시되어 있음 ( 이 주소로 시도했다가 튕겼다고 표시)
                  # 로그인 후 next 로 보내려면 코드 추가해 주면 됨 (accounts/views.py 에)
def create(request):
    if request.method =='POST':
        #post_form = PostForm(request.POST, request.FILES)
        
        post_form = PostForm(request.POST)  # post_form 에는 더이상 이미지파일이 올라가지 않으므로 files 삭제
        image_formset = ImageFormSet(request.POST, request.FILES) # 이미지폼은 post 도 있어야 함(왜인지는 잘...-_-)
        
        if post_form.is_valid() and image_formset.is_valid():  # 저장해도 되는 값이 들어왔으면
            post = post_form.save(commit=False)  # 객체를 만들었으나, 아직 DB에 저장은 x (commit=False 덕분에)
            post.user = request.user  # post 라는 객체의 user 칸에  request 의 user 를 가져와서 받아줌
            
            # post 와 이미지가 1:n 관계라서, post 가 먼저 존재해야, 이미지가 만들어짐
            with transaction.atomic():   # import 해야함
            # 1️⃣ 일단 post 를 만들어야한다
                post.save()  # 저장 = 실제 DB 에 반영
                
                # 2️⃣그후에 image를 저장할 수 있다
                image_formset.instance = post  # image_formset 은 이미지를 만들기 위한 애긴 한데, 3개를 한꺼번에 wrap 해뒀음(extra=3)
                                               # 꺼내기 위해서, instance 붙여줌?
                                               # 근데 post.save() 라는 코드를 실행하고, 확실히 저장을 확인한 뒤에, 다음 문장을 실행하는 게 아니라서
                                               # 오류가 생길 수 있다. 즉 실제 db에서는 이미지가 먼저 저장되고, post 가 저장될 수 있다는 의미
                                               # 이걸 막기위하여, 장고에서 제공하는 method 가  = with transaction.atomic()
                                               
                image_formset.save() # 부모에 대한 정보를 넣고, save 한다 라고 일단 이해를 하라고 하심
                        
                                    
            return redirect('posts:list') 
            
        
    else:  # get방식이면
        post_form = PostForm()
        image_formset = ImageFormSet
        
    return render(request, 'posts/form.html', {'post_form' : post_form, 'image_formset':image_formset,})  # 템플릿에서 쓰기 위하여 딕셔너리 key형태로 변수 넘겨줌
    
@login_required        
def delete(request, post_id):
    # post = Post.objects.get(pk=post_id)   # 존재하지 않는 key 로 삭제버튼 누르려고 하면, 에러
    post = get_object_or_404(Post, id=post_id)   # 존재하지 않는 key 로 삭제버튼을 누르려고 하면, page not found 페이지 보여줌
    
    if post.user != request.user:
        return redirect('posts:list')
        
    post.delete()
    return redirect('posts:list')
    
    
@login_required        
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':  # 그냥 submit 버튼 눌렀을 때
        post_form = PostForm(request.POST, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save()
            image_formset.save()  # update 하는 시점에서는 post 가 만들어진 게 확실하니까 transaction 필요 x
            return redirect('posts:list')
        
    else:  # get요청 = 주소창에 주소 입력했을 때
        post_form = PostForm(instance=post)
        image_formset = ImageFormSet(instance=post)
    return render(request, 'posts/form.html', {'post_form':post_form, 'image_formset':image_formset,})

@login_required    
@require_POST    
def comment_create(request, post_id):  # 특정 글에 댓글을 달아야 하니까, post_id 변수 必
    comment_form = CommentForm(request.POST)   # 댓글을 작성하는 건 get 요청이 필요없음. 그러므로 따로 if문 필요 x
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list') # 댓글을 작성하는 페이지가 따로 있는 건 아니고, 해당 글 밑에 그냥 쓰는 거니까 따로 페이지 만들지 x
    

# a 태그는 post 요청을 보낼 수 없다. post 요청은 form 태그만 사용할 수 있음
# post 요청 데코레이터 쓰면, 그냥 삭제버튼만 만들어도 될 걸, form 태그로 바꿔줘야하는 번거로움 있음
# 그러므로, 그냥 get 요청 들어가도 (a 태그의 href 목적지) 삭제 되도록 설정
@require_http_methods(['GET','POST'])
def comment_delete(request, post_id, comment_id): # 주소쓸 때, post_id 가 먼저 들어가므로 변수 순서 지킬 것
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user: # 댓글의 주인이 아니면
        return redirect('posts:list')  # 목록으로 돌려보내라
        
    comment.delete()
    return redirect('posts:list')
    
@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all():  # post 를 좋아한 사람들 안에 현재 로그인한 사람이 있으면
        post.like_users.remove(request.user)  # 좋아요 취소
    
    else:
        post.like_users.add(request.user) # 현재 로그인한 유저가 해당 포스터를 좋아요 누르는 행위
                                          # post.like_users  (포스터를 좋아한 유저들 목록에)  add(request.user) 로그인한 user 를 더해
    
    
    return redirect('posts:list')