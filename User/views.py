from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile, Video, Question
from .forms import  CustomUserCreationForm


def profiles_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})


def video_list_view(request):
    query = request.GET.get('q')
    if query:
        videos = Video.objects.filter(title__icontains=query)
    else:
        videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.views += 1
    video.save()
    return render(request, 'video_detail.html', {'video': video})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
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
        else:
            messages.error(request, 'Ro‘yxatdan o‘tishda xatolik yuz berdi.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                messages.success(request, 'Siz tizimga kirdingiz!')
                return redirect('profile_list')
            messages.error(request, 'Noto‘g‘ri username yoki parol.')
        else:
            messages.error(request, 'Forma to‘ldirishda xatolik.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def single_profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'single_profile.html', {'profile': profile})


def test_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        correct_answers_count = 0
        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer:
                try:
                    answer = question.answers.get(id=selected_answer)
                    if answer.is_correct:
                        correct_answers_count += 1
                except:
                    pass
        request.session['correct_answers_count'] = correct_answers_count
        request.session['total_questions'] = questions.count()
        return redirect('test_result')
    return render(request, 'test_page.html', {'questions': questions})


def test_result(request):
    correct_answers_count = request.session.get('correct_answers_count')
    total_questions = request.session.get('total_questions')
    if correct_answers_count is None or total_questions is None:
        return redirect('test_view')
    return render(request, "test_result.html", {
        "correct_answers_count": correct_answers_count,
        "total_questions": total_questions,
    })


def home(request):
    return render(request, 'home.html')