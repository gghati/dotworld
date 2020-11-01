from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('restapp.urls')),
    path('admin/', admin.site.urls)
]
