from django.test import TestCase
from django.urls import reverse
from .models import Todo
from rest_framework import test, status


class TodoModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Sample Task",
            body="This is a sample body",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Sample Task")
        self.assertEqual(self.todo.body, "This is a sample body")
        self.assertEqual(str(self.todo), "Sample Task")
        self.assertEqual(Todo.objects.count(), 1)


class TodoAPITests(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Sample API Task",
            body="This is a sample API task",
        )
        cls.otherTodo = Todo.objects.create(
            title="Other Sample Task",
            body="This is another sample API Task",
        )
        cls.list_url = reverse("todo_list")
        cls.detail_url = reverse("todo_detail", args=[cls.todo.id])

    def test_todo_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)

    def test_todo_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIsInstance(response.data, list)
        self.assertEqual(response.data["title"], "Sample API Task")
        self.assertEqual(response.data["body"], "This is a sample API task")

    def test_todo_detail_not_found(self):
        response = self.client.get(reverse("todo_detail", args=[10]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
