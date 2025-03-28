from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer


class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
