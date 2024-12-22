# products/urls.py
from django.urls import path
from .views import create_order, order_summary,products
app_name = 'products'
urlpatterns = [
    path("", products, name='product-list'),
    path('create-order/', create_order, name='create_order'),
    path('<int:order_id>/summary/', order_summary, name='order_summary'),
]
