from django.views.generic import TemplateView
from django.shortcuts import render

from .models import DeviceIoT
# Create your views here.

def list_all_devices(request):
    all = DeviceIoT.objects.all()
    return render(request,"devices/list_devices.html",{"devices":all})