from django.urls import path
from . views import *

urlpatterns=[
    path('',homepage),
    path('productdetails/<int:product_id>',productdetails),
    path('products/',show_products),
    path('addtocart/<int:product_id>',add_to_cart),
    path('cart',show_cart_items),
    path('deletecartitem/<int:cart_id>',delete_cart_item),
    path('order/<int:product_id>/<int:cart_id>',order_item),
    path('myorder/',my_order),
    path('esewa_verify',esewa_verify)
]