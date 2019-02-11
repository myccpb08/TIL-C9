from django import forms
from .models import Article   # Article 모델 import 해오기


class ArticleForm(forms.Form):
    title = forms.CharField(label='제목')   # forms 의 CharField 는 max_length 가 필요 없다, 
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'rows' : 5,
        'cols' : 50,
        'placeholder' : '내용을 입력하세요',
    }))                                                             # 이렇게 하면, html form 태그의 required 속성 저절로 (개발자도구에서 수정할 수 없다_)
                                                                     # forms 에는 textfield 없다 → widget 속성으로, textarea 로 변경
                                                                     # attrs 가 없으면 박스가 이상하게 생겨서, 예쁘게 바꿔주려고, attrs 어쩌고 저쩌고 썼음
                                                                     
                                                                     
                                                                     
class ArticleModelForm(forms.ModelForm):    # 모델과 연관된 클래스
    title = forms.CharField(label='제목') # 얘는 써도 되고, 안 써도 되고
    class Meta:     # Meta 는 꼭 Meta 여야 함 ( ArticleModelForm 클래스(자기 품고 있는 클래스)의 정보가 담겨있는 클래스)
        model = Article  # Article 이라는 모델을 건들거임
        fields = ['title', 'content']    # article 의 필드들 써 줌
        