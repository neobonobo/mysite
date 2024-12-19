from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product, Order  # Import Product and Order models

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Add product list to the context
        if self.request.user.is_authenticated:  # Check if the user is logged in
            context['orders'] = Order.objects.filter(user=self.request.user)  # Filter orders for logged-in user
        else:
            context['orders'] = None  # No orders for anonymous users
        return context
