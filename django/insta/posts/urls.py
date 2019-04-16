from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('explore/', views.explore, name='explore'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),   # post_id 라는 변수명은 views.py 에서 받아오는 변수명과 같아야한다
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'), # 어떤 게시글에, 누가 쓴 댓글 삭제할 것인지
    path('<int:post_id>/like/', views.like, name='like'),
    ]