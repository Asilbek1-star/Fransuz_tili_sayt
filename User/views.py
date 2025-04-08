from django.shortcuts import render, get_object_or_404
from .models import Profile, Video

def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})

def video_list_view(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail_view(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'video_list.html', {'video': video})
