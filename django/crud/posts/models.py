from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
#1. Create
# post = Post(title='hello', content ='world!')
# post.save()

#2. Read
#2.1. All
# posts = Post.objects.all()    : 데이터 베이스에 저장된 모든 객체를 가져와서 posts 라는 변수에 저장, 리턴이 리스트로
#2.2 Get one
# post = Post.objects.get(pk=1) : 하나의 포스트

# 2.3 filter (WHERE)
# posts = Post.objects.filter(title='hello').all()
# post = Post.objects.filter(title='hello').first()

#2.4 LIKE
# posts = Post.objects.filter(title__contains='he').all()                                                     

#2.5 order_by(정렬)
# posts = Post.objects.order_by('title').all()  # 오름차순
# posts = Post.objects.order_by('-title').all()  # 내림차순

#2.6 limit & offset
#[offset:offset + limit]
# posts = Post.objects.all()[1:2]

#3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

#4. Update
# post = Post.objects.get(pk=1)
# post.title = 'hi'
# post.save()


