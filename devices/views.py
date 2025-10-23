from django.views.generic import ListView
from django.shortcuts import render

from .models import DeviceIoT
# Create your views here.

class list_all_devices(ListView):
    #all = DeviceIoT.objects.all()
    model = DeviceIoT
    template_name = "devices/list_devices.html"
    context_object_name = 'devices'
