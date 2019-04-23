from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('docs/', get_swagger_view(title='API DOCS')),  # TITLE 필수로 넘겨줘야 함 
    path('musics/', views.music_list),   # 모든 음악 보여주는 list
    path('musics/<int:music_id>/', views.music_detail),
    path('musics/<int:music_id>/comments/', views.comment_create ),
    path('musics/<int:music_id>/comments/<int:comment_id>/', views.comment_update_and_delete),
    path('artists/', views.artist_list),
    path('artists/<int:artist_id>/', views.artist_detail),
    
    ]