from django.urls import path
from .views import BookListAPI

urlpatterns = [
    path("", BookListAPI.as_view(), name="book_list_api"),
]
