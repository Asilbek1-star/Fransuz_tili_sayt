from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Profiles
    path('profile/', views.profiles_list, name='profile_list'),
    path('profile/<str:username>/', views.single_profile, name='single_profile'),
    # Videos
    path('videos/', views.video_list_view, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    # Test
    path('test/', views.test_view, name='test_view'),
    path('test/result/', views.test_result, name='test_result'),
]
