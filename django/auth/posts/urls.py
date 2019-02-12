from django.urls import path
from . import views

app_name = 'posts'  # 이 urls.py 주인은 posts 다



urlpatterns = [
    path('', views.index, name='list'),    # GET
    
    # path('create/',views.create, name='create'),   new 랑 합침
    path('write/', views.new, name='new'), #  GET(new) # POST(create)
    
    path('<int:post_id>/', views.detail, name='detail'),  # GET
    
    path('<int:post_id>/delete/', views.delete, name='delete'), #GET(confirm), POST(delete)
    
    path('<int:post_id>/edit/', views.edit, name='edit'), # GET(edit), POST(update)
    #path('<int:post_id>/update/', views.update, name='update')  edit 으로 합침
    
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete')
    
]