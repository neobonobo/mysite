from django.db import models
from django.conf import settings  # To reference AUTH_USER_MODEL

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, help_text="Unit of the product, e.g., kg, pieces")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.unit}) - {self.price}/unit"


# Order Model
class Order(models.Model):
    STATUS_CHOICES = (
        ('Ordered', 'Ordered'),
        ('Waiting', 'Waiting'),
        ('Delivered', 'Delivered'),
        ('Received', 'Received'),
        ('Settled', 'Settled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Ordered")
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - {self.status}"


# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"

    def get_cost(self):
        return self.product.price * self.quantity
