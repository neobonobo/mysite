from django.db import models
from django.contrib.auth import get_user_model

class Friend(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='friends')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def balance_with(self, friend):
        given = self.given_exchanges.filter(receiver=friend).aggregate(Sum('quantity'))['quantity__sum'] or 0
        received = self.received_exchanges.filter(giver=friend).aggregate(Sum('quantity'))['quantity__sum'] or 0
        return received - given

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, help_text="e.g., kg, piece, bottle")

    def __str__(self):
        return f"{self.name} ({self.unit})"

class ExchangeTransaction(models.Model):
    giver = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name='given_exchanges')
    receiver = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name='received_exchanges')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.giver} gave {self.quantity} {self.item.unit} of {self.item.name} to {self.receiver}"
