# admin.py
from django.contrib import admin
from .models import BaseModel, CoffeeCategory, CoffeeProduct, Customer, Order

admin.site.register(CoffeeCategory)
admin.site.register(CoffeeProduct)
admin.site.register(Customer)
admin.site.register(Order)