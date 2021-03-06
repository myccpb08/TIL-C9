from django import forms
from .models import Post, Comment, Image

class PostForm(forms.ModelForm):  # 사용하려면, views.py에서 import 해줘야함 
    class Meta:
        model = Post    # 어떠한 모델의 폼을 작성할 거니? Post 라는 모델의 폼을 만들거야
        fields = ['content',]   # models.py 에 작성된 Post 클래스의 content 필드와 이미지필드


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
        
ImageFormSet = forms.inlineformset_factory(Post,Image,form=ImageForm,extra=3)
# 첫번째 인자 : 부모 모델 (1:n 관계에서 1 역할, 이미지를 데리고 있을 애 = 글 )
# 두번째 인자 : 생성할 모델 ( 이미지 모델)
# 무슨 폼을 사용하는지
# 몇 개의 이미지폼을 엮을 것인지 = 이미지 폼 3개를 쓸 수 있음

        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'댓글을 작성하세요'}))  
                                         # 클래스 2개 넣고 싶으면 띄어쓰고 쓰면 됨 ex) 'class': 'form-control blue red'
                                         # form-control : form 을 예쁘게 꾸며 주는 
                                         # attrs = attributes 약자
                                         # models.py 에서 textfield 로 만들었는데, 댓글창이 너무 커서 못생겼으니까 작게 바꿔주는 작업
                                         # 한 줄 짜리 input 태그로 바뀜
                                         # content 라는 라벨도 안 보임 (label='') 때문에
                                         # charfield 는 저장할 수 있는 최대 길이가 제한되어 있음 그러므로 보여주는 건 charfield 로 보여주고
                                         # 실제로 저장해주는 형식인 models.py  는 textfield 로 남겨둠
    class Meta:
        model = Comment
        fields = ['content']
        
    