from django.urls import path
from .views import CoffeeCategoryListView, CoffeeProductListView, CustomerListView, OrderListView, coffee_category_list

urlpatterns = [
    path('categories/', CoffeeCategoryListView.as_view(), name='coffeecategory-list'),
    path('products/', CoffeeProductListView.as_view(), name='coffeeproduct-list'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('coffeecategories/', coffee_category_list, name='coffeecategory-list'),
    # Add other URLs as needed
]
