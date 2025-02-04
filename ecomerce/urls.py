
from django.urls import path
from ecomerce import views

urlpatterns = [
path('', views.product_list, name='product_list'),
path('detail/<int:pk>/',views.product_detail, name='product_detail'),
path('customers/',views.customers, name='customers'),
path('customer_detail/',views.customer_detail, name='customer_detail'),
]
