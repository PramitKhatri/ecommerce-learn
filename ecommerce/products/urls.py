from django.urls import path
from . views import *

urlpatterns=[
    # path('',index),
    path('show/',showproduct),
    path('addcategory/',addcategory),
    path('addproduct/',postproduct),
    path('allcategory/',showcategory),
    path('deletecategory/<int:category_id>',deletecategory),
    path('updatecategory/<int:category_id>',updatecategory),
    path('deleteproduct/<int:product_id>',deleteproduct),
    path('updateproduct/<int:product_id>',updateproduct),

]