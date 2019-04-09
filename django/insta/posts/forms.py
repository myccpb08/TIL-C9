from django import forms
from .models import Post

class PostForm(forms.ModelForm):  # 사용하려면, views.py에서 import 해줘야함 
    class Meta:
        model = Post    # 어떠한 모델의 폼을 작성할 거니? Post 라는 모델의 폼을 만들거야
        fields = ['content','image',]   # models.py 에 작성된 Post 클래스의 content 필드와 이미지필드