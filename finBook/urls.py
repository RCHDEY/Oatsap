
from django.contrib import admin
from django.urls import path
from Oatsap.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name="home")
]
