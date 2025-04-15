from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile, Video, Question
from .forms import CustomUserCreationForm



def profiles_list(request):
    profile = Profile.objects.annotate(total_score=Sum('user__testresult__score')).order_by('-total_score')
    return render(request, 'profile_list.html', {
        'profiles': Profile.objects.all(),
        'profile': profile,
    })


def video_list_view(request):
    query = request.GET.get('q')
    videos = Video.objects.filter(title__icontains=query) if query else Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.views += 1
    video.save()
    return render(request, 'video_detail.html', {'video': video})


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                name=user.username,
                level='A1',
                phone='',
                bio='No bio yet'
            )
            login(request, user)
            messages.success(request, 'Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz!')
            return redirect('profile_list')
        messages.error(request, 'Ro‘yxatdan o‘tishda xatolik yuz berdi.')
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.success(request, 'Siz tizimga kirdingiz!')
                return redirect('home')
            messages.error(request, 'Noto‘g‘ri username yoki parol.')
        else:
            messages.error(request, 'Forma to‘ldirishda xatolik.')
    return render(request, 'login.html', {'form': form})


def single_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    all_profiles = Profile.objects.all()
    top_profiles = sorted(all_profiles, key=lambda p: p.total_score(), reverse=True)[:5]

    return render(request, 'single_profile.html', {
        'profile': profile,
        'top_profiles': top_profiles,
    })


def test_view(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        correct_answers = 0

        # Loop through all questions and check if the correct answer is selected
        for q in questions:
            answer_id = request.POST.get(f'question_{q.id}')
            if answer_id:
                if q.answers.filter(id=answer_id, is_correct=True).exists():
                    correct_answers += 1

        # Optionally, display the result to the user
        return render(request, 'test_result.html',
                      {'correct_answers': correct_answers, 'total_questions': questions.count()})

    # Render the test page with the list of questions
    return render(request, 'test_page.html', {'questions': questions})


def test_result(request):
    correct = request.session.get('correct_answers_count')
    total = request.session.get('total_questions')

    if correct is None or total is None:
        messages.error(request, "Test hali yozilmagan!")
        return redirect('test_view')

    return render(request, "test_result.html", {
        "correct_answers_count": correct,
        "total_questions": total,
    })


def home(request):
    return render(request, 'home.html', {
        'trending': Video.objects.order_by('-views')[:6],
        'latest_videos': Video.objects.order_by('-created_at')[:5],
        'recommended_videos': Video.objects.order_by('?')[:5],
    })


def logout_view(request):
    logout(request)
    return redirect('home')