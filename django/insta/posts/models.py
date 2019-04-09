from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def post_image_path(instance, filename):
    return f'posts/{instance.content}/{filename}'
    
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = ProcessedImageField(
        upload_to = post_image_path,
        processors=[ResizeToFill(600,600)], # 처리할 작업 목록
        format = 'JPEG', # 저장 포맷
        options = {'quality':90}, # 옵션
        )