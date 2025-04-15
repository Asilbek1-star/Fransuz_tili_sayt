from django.test import TestCase
from django.urls import reverse
from .models import Profile, Video

class ProfileTests(TestCase):
    def setUp(self):
        self.user = Profile.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        Profile.objects.create(
            user=self.user,
            name="Test User",
            level="A1",
            phone="123456789",
            bio="This is a test bio"
        )

        self.video = Video.objects.create(
            title="Test Video",
            level="A1",
            video_file="videos/test_video.mp4",
            category="grammar"
        )

    def test_profile_view(self):
        response = self.client.get(reverse('profile_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")

    def test_video_list_view(self):
        response = self.client.get(reverse('video_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Video")

    def test_video_detail_view(self):
        response = self.client.get(reverse('video_detail', args=[self.video.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Video")
