from django.test import TestCase
from django.urls import reverse
from .models import Video


class TestHomePageMessage(TestCase):

    def test_app_title_message_shown_on_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, 'Horse Videos')


class TestAddVideos(TestCase):

    def test_add_video(self):
        valid_video = {
            'name': 'New Horse Shopping',
            'url': 'https://www.youtube.com/watch?v=ZxJ0A5xcqEI',
            'notes': 'New Horse Shopping'
        }
        url = reverse('add_video')
        response = self.client.post(url, data=valid_video, follow=True)

        self.assertTemplateUsed('video_collection/video_list.html')
        self.assertContains(response, 'New Horse Shopping')
        self.assertContains(response, 'https://www.youtube.com/watch?v=ZxJ0A5xcqEI')
        self.assertContains(response, 'New Horse Shopping')

        video_count = Video.objects.count()
        self.assertEqual(1, video_count)

        video = Video.objects.first()

        self.assertEqual(video.name, 'New Horse Shopping')
        self.assertEqual(video.url, 'https://www.youtube.com/watch?v=ZxJ0A5xcqEI')
        self.assertEqual(video.notes, 'New Horse Shopping')
        self.assertEqual(video.video_id, 'ZxJ0A5xcqEI')

    def test_add_video_url_not_added(self):

        invalid_video_urls = [
            'https://www.youtube.com/watch',
            'https://www.youtube.com/watch?',
            'https://www.youtube.com/watch?abc=123',
            'https://www.youtube.com/watch?v=',
            'https://www.github.com',
            'https://www.minneapolis.edu',
            'https://www.minneapolis.edu/watch?v=ZxJ0A5xcqEI'
        ]

        for invalid_video_url in invalid_video_urls:

            new_video = {
                'name': 'example',
                'url': invalid_video_url,
                'notes': 'example notes'
            }

            url = reverse('add_video')
            response = self.client.post(url, new_video)

            self.assertTemplateNotUsed('video_collection/add.html')

            messages = response.context['messages']
            message_texts = [message.message for message in messages]

            self.assertIn('Invalid YouTube URL', message_texts)
            self.assertIn('Please check the data entered.', message_texts)

            video_count = Video.objects.count()
            self.assertEqual(0, video_count)


class TestVideoList(TestCase):
    pass


class TestVideoSearch(TestCase):
    pass


class TestVideoModel(TestCase):
    pass
