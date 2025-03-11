from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from books.models import Book


class BookAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django Tutorial",
            subtitle="A guide to mastering Django",
            author="Django",
            isbn="012-123456789",
        )

    def test_book_api_view(self):
        response = self.client.get(reverse("book_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
