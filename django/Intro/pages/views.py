from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
#Template 변수    
def dinner(request):
    menu = ["족발", "햄버거", "치킨", "초밥"]
    pick = random.choice(menu)
    return render(request,'dinner.html', {'dinner': pick})
    
#Variable routing (주소를 변수처럼 사용하기)
def hello(request, name): # 주소로부터 받고 싶은 변수의 이름을 정해야 한다 , 이 경우 name
    return render(request, 'hello.html', {'name':name})
    
def luckynum(request, birth):
    num=[i for i in range(100)]
    pickk = random.choice(num)
    return render(request,'lucky.html',{'number': pickk,'bir':birth})
    
# 바디 內 Form tag 이용
def throw(request):
    return render(request,'throw.html')
    
def catch(request):  # request 안에 message 들어 있음
    message = request.GET.get('message')    # GET = throw.html 內 method 의 "get"      .get= 딕셔너리의?
    return render(request,'catch.html', {'message':message})
    ## 내가 /throw 페이지에서  '야' 라고 입력하면 message = 야 라고 되어 있어서 .get('message') 하면 야 가져옴?
    

# Form 외부로 요청
def naver(request):
    return render(request,'naver.html')
    
# Bootstrap
def bootstrap(request):
    return render(request, 'bootstrap.html')