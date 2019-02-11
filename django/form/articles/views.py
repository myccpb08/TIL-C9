from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)    # POST 로 받아 들어온 데이터로, form 의 title 과 content  를 미리 채워둔다

        if form.is_valid():
            article = form.save()
            #title = form.cleaned_data.get('title')
            #content = form.cleaned_data.get('content')
        
            # title = request.POST.get('title') : 얘네는 검증안된, 데이터였음
            # content = request.POST.get('content') : 얘도
            
            #article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
            
    else:
        form = ArticleModelForm()    # forms 의 ArticleForm 을 받아옴
        
    return render(request, 'form.html', {'form':form})  # 템플릿변수로 form 을 넘겨준다
        
        

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article': article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article) # 이렇게 적으면, 수정페이지에, 원래 적혀있는 글 보여줌

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
            
    else:
        form = ArticleModelForm(instance=article)  # 여기서 article 은 def 밑에 쓴 article
        
    return render(request, 'form.html', {'form':form})