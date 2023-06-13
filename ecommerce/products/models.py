from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

# here you make the structure of the table in DB
class Product(models.Model):
    product_name=models.CharField(max_length=100) #charfield is for varchar
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_description=models.TextField()
    product_image=models.FileField(upload_to='static/uploads',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True) #auto_now_add puts the date automatically on the day its created
    
    def __str__(self):
        return self.product_name

