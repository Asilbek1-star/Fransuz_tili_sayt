from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profiles_list, name='profile_list'),
    path('videos/', views.video_list_view, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/<str:username>/', views.single_profile, name='single_profile'),
    path('test/', views.test_view, name='test_view'),
    path('test/result/', views.test_result, name='test_result'),
    path('', views.home, name='home'),
]