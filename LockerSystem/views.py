
from django.shortcuts import render


def home_page_view(request): # new
    return render(request, "home.html")