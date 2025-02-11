from django.urls import path
from customers.views import customer_detail,customers_list,delete_customer,edit_customer,add_customer

urlpatterns = [

path('customers/',customers_list, name='customers'),
path('customer_detail/<int:pk>/',customer_detail, name='customer_detail'),
path('delete_customer/<int:pk>/',delete_customer, name='delete_customer'),
path('edit_customer/<int:pk>/',edit_customer, name='edit_customer'),
path('customer_add/',add_customer, name='add_customer'),
]
