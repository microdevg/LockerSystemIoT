from django.urls import path
from .views import list_all_devices

urlpatterns = [path("all", list_all_devices, name="allDevices")]