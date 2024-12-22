from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product, Order, OrderItem
from .forms import OrderItemForm

@login_required
def create_order(request):
    if request.method == "POST":
        selected_products = request.POST.getlist('products')
        quantities = request.POST.getlist('quantity')

        if not selected_products:
            return HttpResponse("No products selected.")

        # Create a new order
        order = Order.objects.create(user=request.user)

        # Add selected products to the order
        for product_id, quantity in zip(selected_products, quantities):
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=int(quantity))

        return redirect('order_summary', order_id=order.id)

    # Fetch all products
    products = Product.objects.all()
    return render(request, 'products/create_order.html', {'products': products})
@login_required
def order_summary(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_summary.html', {'order': order})

def products(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
