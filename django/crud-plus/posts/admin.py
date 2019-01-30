from django.contrib import admin
from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):   # admin.ModelAdmin 을 상속받은 클래스
    list_display = ('title','content',)

# Register your models here.
admin.site.register(Post, PostAdmin) # 위 클래스명 적어준 거. 이렇게 하면 관리자페이지에서 제목과 내용 보임
admin.site.register(Comment)
