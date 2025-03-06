from django.urls import path
from .views import home_page_view, AboutPageView

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
