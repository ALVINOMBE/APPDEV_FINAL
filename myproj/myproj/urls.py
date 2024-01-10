from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from couzycup.views import CoffeeCategoryListView, CoffeeProductListView, CustomerListView, OrderListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('categories/', CoffeeCategoryListView.as_view(), name='coffeecategory-list'),
    path('products/', CoffeeProductListView.as_view(), name='coffeeproduct-list'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    # Add other URLs as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


