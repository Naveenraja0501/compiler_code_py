from django.contrib import admin
from django.urls import path
from compiler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
