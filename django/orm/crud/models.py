from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
# 정리
# class Post: Django 에서는 model 이라고 부름
            # DB에서는 table 이라고 부름
            
# post = Post() : Post 클래스의 인스턴스 = post
            # Django 에서는 instance or Object 라고 부름 ( ∵ OOP 에서 Object)
            # DB에서는 Record or Row

# title : Django 에서는 Field
         # DB 에서는 Column 이라고 불림
         
# 마이그레이션
# ./manage.py makemigrations
# ./manage.py migrate

# CRUD
# 1. Create
#   방법1) 
#       post = Post(title='hello-1')
#       post.save()

#   방법2)
#       post2 = Post.objects.create(title='hello-2')

#   방법3)
#       post3 = Post()
#       post3.title = 'hello-3'
#       post3.save()

# 2. Read
# 2-1. All
# posts = Post.objects.all()

# 2-2. One
# 방법 1
# post = Post.objects.get(pk=1)  : id=1, title='hello-1' 도 가능
# 만약에 title='hello-1' 인 글이 여러 개 있으면 get 은 id 번호가 가장 낮은 거 1개만 찾아줌

# 방법 2 (views.py 한정)
# from django.shortcuts import get_objects_or_404
# post = get_object_or_404(Post, pk=1)  # id=1, title='hello-1' 도 가능

# 방법 3
# post = Post.objects.filter(pk=1)[0]  # id=1, title='hello-1' 도 가능
# post = Post.objects.filter(pk=1).first()  # last()  도 있음
# 만약에 title='hello-1' 인 글이 여러 개 있으면 filter 는 모든 글을 가져옴
# 모든 글을 가져와서 리스트에 들어있을 테니까 (post 에) 뒤에 [0] 을 붙이면, 아이디 가장 작은 글 가져옴

# 2-3. Where(filter)
# posts = Post.objects.filter(title='hello-1')
# post = Post.objects.filter(title='hello-1').first()  # 또는 [0]

# LIKE
# posts = Post.objects.filter(title__contains='lo')

# 정렬 : order_by
# posts = Post.objects.order_by('title')  # 제목 오름차순
# posts = Post.objects.order_by('-title')  # 제목 내림차순

# offset & limit  : offset = 앞에 빈 공간을 두는 것
# post = Post.objects.all()[0]  #=> offset=0 limit=1
# post = Post.objects.all()[1]  #=> offset=1 limit=1
# post = Post.objects.all()[1:3]  :  # offset = 1 이고, limit = 2
# post = Post.objects.all()[offset:offset+limit]


# 3. update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save()  # 실제 데이터베이스에 저장


# 4. Delete
# post = Post.objects.get(pk=1)
# post.delete()
# 한 줄로 쓰고 싶다면 
# Post.objects.get(pk=1).delete()