from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a dummy text")

    def test_post_content(self):
        self.assertEqual(self.post.text, "This is a dummy text")

    def test_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    def test_used_template(self):
        response = self.client.get(reverse("post_list"))
        self.assertTemplateUsed(response, "post_list.html")

    def test_template_content(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, "This is a dummy text")
