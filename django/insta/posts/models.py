from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


def post_image_path(instance, filename):
    return f'posts/{instance.content}/{filename}'
    
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
                                    # 외래키: 이 테이블 外 에서 가져온 어떤 키를 여기에 담아둔다
                                    # 원래는 ForeignKey(User) : 장고는 기본적으로 User 라는 테이블을 알아서 만들어 둠
                                    # 근데 장고가 만든 User 테이블말고, 자기가 customize 한 테이블 쓰고 싶으면
                                    # settings 를 import 해서 바꿔주면 됨 : User → settings.AUTH_USER_MODEL
                                    # on_delete = models.CASCADE 란? 1:N 관계에서 1의 정보가 삭제되면 N 도 삭제된다 (탈퇴하면 글 다 삭제)
                                    # 그 외 여러가지 옵션이 있음 (공식문서 model field reference)
                                    # PROTECT : n이 있으면 1을 삭제 못함  ( 글 남아있으면 탈퇴 못함)
                                    # SET_NULL : 주인이 없는 상태로 그냥 둠  (CASCADE 보다 더 빈도) : 탈퇴했으나 카페에 글은 有
                                    # SET_DEFAULT : 기본값으로 바꿈
                                    # SET() : 내가 설정한 걸로 바꿈
                                    # DO_NOTHING : 그냥 아무것도 안 함
    content = models.TextField()
    image = ProcessedImageField(
        upload_to = post_image_path,
        processors=[ResizeToFill(600,600)], # 처리할 작업 목록
        format = 'JPEG', # 저장 포맷
        options = {'quality':90}, # 옵션
        )
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')  # 좋아요 누른 user 들
        
        
class Comment(models.Model): # 2중 1:N    [글 : 댓글입력자 = 글 : 댓글 = 1:N]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # foreignkey 의 첫번째 인자 = 어떤 테이블과 관계를 맺을 것인지
                                                                                   # on_delete 옵션 必
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    
