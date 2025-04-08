from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('videos/', views.video_list_view, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail_view, name='video_detail'),
]
