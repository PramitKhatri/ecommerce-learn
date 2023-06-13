from django.forms import ModelForm
from . models import *

# to install the bootstarp form of django use: 'py -m pip install django-bootstrap-form' in terminal or 'pip install django-bootstrap-form'
# to update pip use: python.exe -m pip install --upgrade pip
class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        
