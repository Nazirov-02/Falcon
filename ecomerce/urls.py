
from django.urls import path
from ecomerce.views import product_detail,product_list,comment,search


urlpatterns = [
path('',product_list, name='product_list'),
path('detail/<int:pk>/',product_detail, name='product_detail'),
path('comment/<int:pk>',comment, name='comment-detail'),
path('product_search', search,name='product_search'),
]
