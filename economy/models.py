from django.db import models
from django.contrib.auth import get_user_model

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Food", "Transport"
    description = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()  # Make this editable for changes
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the whole expense
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Expense on {self.date} for {self.category.name} - {self.amount}"

