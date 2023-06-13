from django.forms import ModelForm
from .models import *


# modelform creates a form automatically to input the given fields
class OrderForm(ModelForm):
    class Meta:
        model=Order  #this is from models.py  userpage
        fields=['quantity','payment_method','phone_no','address']
