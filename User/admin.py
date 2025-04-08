from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile, Video




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'level', 'phone', 'user_email', 'is_staff', 'is_active')
    list_filter = ('user__is_staff', 'user__is_active')  # Filter based on User model
    ordering = ('user__username',)

    def user_email(self, obj):
        return obj.user.email  # Access email from the related User model
    user_email.admin_order_field = 'user__email'  # Enable ordering by email

    def is_staff(self, obj):
        return obj.user.is_staff  # Access is_staff from the related User model
    is_staff.boolean = True  # Display as a boolean field

    def is_active(self, obj):
        return obj.user.is_active  # Access is_active from the related User model
    is_active.boolean = True  # Display as a boolean field




class VedioAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'video_file')


admin.site.register(Video, VedioAdmin)
admin.site.register(Profile, ProfileAdmin)


