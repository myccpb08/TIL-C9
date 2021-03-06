from django.db import models
from imagekit.models import ProcessedImageField   # 원래 models.ImageField 를 대체할 아이
from imagekit.processors import ResizeToFill # 이미지가 업로드되는 과정에서 어떤 조작과정을 거칠지

# ResizeToFill : 300, 300 맞추고 넘치는 부분 잘라냄
# ResizeToFit : 300, 300 맞추고 남는 부분은 빈 공간으로 둠

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #image = models.ImageField(blank=True) # 이 칼럼에는 빈칸이어도 된다
    image = ProcessedImageField(
            upload_to = 'posts/images',      # 어디에 업로드 될 것인지 = 저장위치   
            processors = [ResizeToFill(300,300)],  # 업로드 되면 무슨 처리과정을 거칠지. 가로 세로 300으로 바꿔/  이 값들 단순 변경은 migrations 안 해도 됨
            format='JPEG', # 저장 포맷 (확장자)
            options={'quality':90}, # 저장 포맷 관련 옵션 : jpeg 는 압축스타일이라 얼마나 퀄리티로 압축할지
        )
        
    created_at = models.DateTimeField(auto_now_add=True) # 언제 生되었는지에 대한 정보: 하나의 데이터가 생성될 때(딱 한 번) 현재 시간을 넣어
    updated_at = models.DateTimeField(auto_now=True) # 언제 업데이트 되었는지에 대한 정보 : 변경이 될 때 마다, 현재 시각
    
    def __str__(self):
        return self.title
    
# 댓글 기능    
# Post : Comment =1: N
class Comment(models.Model):
    # 어떤 게시글에 대한 댓글인가 = 게시글 정보
    # 댓글 쓸 글 = post ( 외부 테이블 foreignkey 로부터 id 를 가져와서 게시글 지정_)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)  # 외부키 = foreignkey (=다른 테이블의 키 값을 가져올 거)
                                                             # 무슨 외부 테이블 쓸거야? Post
                                                             # on_delete : post가 사라졌을 때 (내가 댓글 단 글이 없어졌을 때)
                                                                           #댓글을 어떻게 처리할 것인지
                                                             # models.CASCADE : 글 없어지면, 댓글도 같이 삭제
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


