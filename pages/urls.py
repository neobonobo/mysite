# pages/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import HomePageView,custom_redirect_view,user_homepage,send_message,log_smoke

app_name = 'pages'  # Register the namespace
urlpatterns = [
    path('home',HomePageView.as_view(), name='home'),
    path("send-message/", send_message, name="send_message"),
    path('log-smoke/', log_smoke, name='log_smoke'),
    path('redirect/', custom_redirect_view),
    path('<str:username>/', user_homepage, name='user_homepage'),
    path('', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

