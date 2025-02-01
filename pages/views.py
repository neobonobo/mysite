from django.shortcuts import redirect,render,get_object_or_404
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.views.generic import TemplateView
from products.models import Product, Order  # Import Product and Order models
from chronos.models import ImportantDate,Todo
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from products.models import Product
from products.models import Order, OrderItem
from economy.models import Expense, ExpenseCategory

@login_required
def user_homepage(request, username):
    if request.user.username.lower() != username.lower():
        return redirect(f"/{request.user.username}/")
    # Restrict access to diablo's page
    if username.lower() == "diablo" and request.user.username.lower() != "diablo":
        return redirect(f"/{request.user.username}/")  # Redirect unauthorized users

    # Handle form submission for a new order
    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity = request.POST.get("quantity")
        if product_id and quantity:
            product = Product.objects.get(id=product_id)
            order = Order.objects.create(user=request.user, status="Ordered", details="New order created")
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
            return redirect(f"/{username}/")

    # Fetch available products and user's past orders
    products = Product.objects.all()
    expenses = Expense.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, f"pages/{username.lower()}.html", {
        "username": username,
        "products": products,
        "orders": orders,
        "expenses":expenses
    })
def custom_redirect_view(request):
    if request.user.is_authenticated:
        return redirect(f'/{request.user.username}/')
    return redirect('login')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Add product list to the context
        if self.request.user.is_authenticated:  # Check if the user is logged in
            context['orders'] = Order.objects.filter(user=self.request.user)  # Filter orders for logged-in user
        else:
            context['orders'] = None  # No orders for anonymous users
        if self.request.user.is_authenticated:  # Check if the user is logged in
            context['dates'] = ImportantDate.objects.all().order_by('-date')
        else:
            context['dates'] = None
        if self.request.user.is_authenticated:  # Check if the user is logged in
            context['todos'] = Todo.objects.all().order_by('-created_at')
        else:
            context['todos'] = None

# Handle todos grouping
        if self.request.user.is_authenticated:
            today = date.today()
            tomorrow = today + timedelta(days=1)

            # Separate todos based on their due date
            context['today_todos'] = Todo.objects.filter(user=self.request.user, due_date=today).order_by('-created_at')
            context['tomorrow_todos'] = Todo.objects.filter(user=self.request.user, due_date=tomorrow).order_by('-created_at')
            context['other_todos'] = Todo.objects.filter(
                user=self.request.user
            ).exclude(due_date__in=[today, tomorrow]).order_by('-created_at')
        else:
            context['today_todos'] = None
            context['tomorrow_todos'] = None
            context['other_todos'] = None
        return context
@login_required
def toggle_todo_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('home')  # Redirect to home page
