from django.urls import path
from . import views

urlpatterns =[
    path('main/',views.home),
    path('admin/',views.welcome),
    path('signup/', views.sign_page),
    path('login/signup/', views.sign_page),
    path('login/', views.login_page)

]