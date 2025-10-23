from django.views.generic import TemplateView
from django.shortcuts import render



def home_page_view(request):

    return render(request, "home.html")

class AboutPageView(TemplateView):
    template_name = "about.html"


