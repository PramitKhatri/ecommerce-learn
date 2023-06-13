from django.urls import path
from . views import *

urlpatterns=[
    path('register/',register_user),
    path('login/',post_login),
    path('logout/',logout_user)
]