from django.contrib import admin
from .models import Friend, Item, ExchangeTransaction

admin.site.register(Friend)
admin.site.register(Item)
admin.site.register(ExchangeTransaction)

# Register your models here.
