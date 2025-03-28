from django.db import models


class Book(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
