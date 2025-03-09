from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="janedoe", email=None, password="secret"
        )

        cls.post = Post.objects.create(
            title="Test Django Model!",
            author=cls.user,
            body="Lorem ipsum dolor, sit amet consectetur adipisicing elit",
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Test Django Model!")
        self.assertEqual(
            self.post.body, "Lorem ipsum dolor, sit amet consectetur adipisicing elit"
        )
        self.assertEqual(self.post.author.username, "janedoe")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_listview_url_exists(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_detailview_url_exists(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertContains(
            response, "Lorem ipsum dolor, sit amet consectetur adipisicing elit"
        )
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(self.post.get_absolute_url())
        err_response = self.client.get("/post/1000/")
        self.assertContains(response, "Test Django Model!")
        self.assertTemplateUsed(response, "post-detail.html")
        self.assertEqual(err_response.status_code, 404)
