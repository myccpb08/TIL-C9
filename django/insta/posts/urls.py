from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/delete/', views.delete, name='delete'),   # post_id 라는 변수명은 views.py 에서 받아오는 변수명과 같아야한다
    ]