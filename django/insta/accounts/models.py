from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    # user 삭제되면 프로필도 필요없으니 CASCADE 옵션
    # 아래, 닉네임과, 소개, 이미지는 회원가입시 필수사항이 아니므로 빈칸 허용
    
    nickname = models.CharField(max_length=40, blank=True) # 닉네임작성
    introduction = models.TextField(blank=True) # 자기소개 작성
    image = ProcessedImageField( # 프로필이미지
                blank=True,
                upload_to = 'profile/images',  #이미지 저장 위치
                processors=[ResizeToFill(300,300)], # 처리할 작업 목록
                format = 'JPEG', # 저장 포맷
                options = {'quality':90}, # 옵션
        )
        


class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings') 
    # 이렇게 하면 장고가 제공하는 USER 클래스가 들어가있음
    # 후에, 우리가 만든 User 로 바꿔주는 설정 해줘야됨
    # 그래야 오류가 안 남
    # user.followings 랑 user.followrs 둘 다 가능하다. (무슨말이지?)
                                                            