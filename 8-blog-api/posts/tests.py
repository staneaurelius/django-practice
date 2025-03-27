from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@testmail.com", password="admin321"
        )

        cls.post = Post.objects.create(
            author=cls.user, title="Sample post title", body="Sample post content"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Sample post title")
        self.assertEqual(self.post.body, "Sample post content")
        self.assertEqual(str(self.post), "Sample post title")
