# pages/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import HomePageView,custom_redirect_view,user_homepage

app_name = 'pages'  # Register the namespace
urlpatterns = [
    path('home',HomePageView.as_view(), name='home'),
    path('redirect/', custom_redirect_view),
    path('<str:username>/', user_homepage, name='user_homepage'),
    path('', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

