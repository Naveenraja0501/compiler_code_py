from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('compiler.urls')),
    path('', include('compiler.urls')),
]
