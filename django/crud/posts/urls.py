from django.urls import path
from . import views

urlpatterns = [
    path('naver/<str:q>/', views.naver),
    path('', views.index),
    path('create/',views.create),
    path('new/', views.new),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
    
]