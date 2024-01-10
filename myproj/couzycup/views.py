from django.shortcuts import render

# Create your views here.
from django.db import models
from django.views.generic import ListView
from .models import CoffeeCategory, CoffeeProduct, Customer, Order

class CoffeeCategoryListView(ListView):
    model = CoffeeCategory
    template_name = 'coffeecategory_list.html'    

class CoffeeProductListView(ListView):
    model = CoffeeProduct
    template_name = 'coffeeproduct_list.html'
    product_image = models.ImageField(upload_to='coffee_images/', null=True, blank=True)

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    
def home(request):
    return render(request, 'base.html')

# views.py
from django.shortcuts import render
from .models import CoffeeCategory

def coffee_category_list(request):
    categories = CoffeeCategory.objects.all()
    return render(request, 'coffeecategory_list.html', {'categories': categories})

