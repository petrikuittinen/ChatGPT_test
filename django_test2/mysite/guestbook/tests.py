from django.test import TestCase
from django.urls import reverse
from guestbook.models import Post

class GuestbookViewTests(TestCase):
    def test_guestbook_view(self):
        response = self.client.get(reverse('guestbook:guestbook'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guestbook/guestbook.html')

    def test_guestbook_create_post(self):
        response = self.client.post(reverse('guestbook:add_guestbook_post'), {'author': 'test_author', 'message': 'test_message'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.author, 'test_author')
        self.assertEqual(post.message, 'test_message')
        self.assertRedirects(response, reverse('guestbook:guestbook'))

