from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django Tutorial",
            subtitle="A guide to mastering Django",
            author="Django",
            isbn="012-123456789",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Django Tutorial")
        self.assertEqual(self.book.subtitle, "A guide to mastering Django")
        self.assertEqual(self.book.author, "Django")
        self.assertEqual(self.book.isbn, "012-123456789")

    def test_book_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Tutorial")
        self.assertTemplateUsed(response, "books/book-list.html")
