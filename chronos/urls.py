from django.urls import path
from . import views
from pages.views import toggle_todo_status

urlpatterns = [
    path('', views.important_date_list, name='important_date_list'),
    path('dates/<int:pk>/', views.important_date_detail, name='important_date_detail'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('toggle/<int:pk>/', toggle_todo_status, name='toggle_todo_status'),
]
