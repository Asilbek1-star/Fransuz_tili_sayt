from django.contrib import admin
from .models import Profile, Video, Question, Answer


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'level', 'phone', 'user_email', 'is_staff', 'is_active')
    list_filter = ('user__is_staff', 'user__is_active')
    ordering = ('user__username',)

    def user_email(self, obj):
        return obj.user.email
    user_email.admin_order_field = 'user__email'

    def is_staff(self, obj):
        return obj.user.is_staff
    is_staff.boolean = True

    def is_active(self, obj):
        return obj.user.is_active
    is_active.boolean = True


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'category', 'views', 'created_at')
    search_fields = ('title', 'description')


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
