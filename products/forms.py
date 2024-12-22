# products/forms.py
from django import forms
from .models import Product, OrderItem


class OrderForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Products"
    )


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }
