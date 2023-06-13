from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.core.validators import *

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    PAYMENT=(
        ('Cash on Delivery','Cash on Delivery'), #here the front one is to show the user and the later one is to store in database
        ('Esewa','Esewa'),
        ('Khalti','Khalti')
    )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField(null=True)
    status=models.CharField(default='Pending',max_length=200)
    payment_method=models.CharField(max_length=100,choices=PAYMENT)
    payment_status=models.BooleanField(default=False,null=True)
    phone_no=models.CharField(max_length=20,validators=[MinLengthValidator(9),MaxLengthValidator(20)])
    address=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
