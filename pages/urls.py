# pages/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='pages/home.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

