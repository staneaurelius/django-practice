from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Homepage")


def about_page_view(request):
    context = {
        "name": "Ausar",
        "age": 24,
    }
    return render(request, "pages/about.html", context)
