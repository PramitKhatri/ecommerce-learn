from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product,Category
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userpage.auth import admin_only
# Create your views here.

def index(request):
    return HttpResponse('this is from products app')

# to fetch all data from the database
@login_required
@admin_only
def showproduct(request):
    products=Product.objects.all() #Product.object.all() is same as SELECT * FROM Product in SQL. it is the python version ;)
    context={
        'products':products
    }
    return render(request,'products/product.html',context)

# to show add category form and post category
@login_required
@admin_only
def addcategory(request):
    # data processing
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'category added')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request, messages.ERROR, 'failed to add category')
            return render(request, 'products/addcategory.html',{'forms':form})

    context={
        'forms':CategoryForm
    }
    # to load add category forms
    return render(request, 'products/addcategory.html',context)


@login_required
@admin_only
def postproduct(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'product added')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request, messages.ERROR, 'failed to add product')
            return render(request, 'products/addproduct.html',{'forms':form})
    
    context={
        'forms':ProductForm
    }
    return render(request, 'products/addproduct.html',context)

    # to show categories in allcategory.html
@login_required
@admin_only
def showcategory(request):
    category=Category.objects.all()

    context={
        'categories':category
    }
    return render(request, 'products/allcategory.html',context)

# delete the category
@login_required
@admin_only
def deletecategory(request,category_id):
    category=Category.objects.get(id=category_id) # get() is for gettting single elements to delete them individually
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'category deleted')
    return redirect('/products/allcategory')


# update category
@login_required
@admin_only
def updatecategory(request,category_id):
    instance=Category.objects.get(id=category_id)  #instance is a variable and can be anything

    if request.method=='POST':
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'çategory updated')
            return redirect('/products/allcategory')
        else:
            messages.add_message(request, messages.ERROR, 'failed to update category')
            return render(request, 'products/updatecategory.html',{'forms':form})


    context={
        'forms':CategoryForm(instance=instance)  #the front instance is parameter name or smth and the back one is the variable
    }
    return render(request, 'products/updatecategory.html',context)


# delete the products
@login_required
@admin_only
def deleteproduct(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'product deleted')
    return redirect('/products/show')
    
# update product
@login_required
@admin_only
def updateproduct(request,product_id):
    instance=Product.objects.get(id=product_id)  #instance is a variable and can be anything

    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'product updated')
            return redirect('/products/show')
        else:
            messages.add_message(request, messages.ERROR, 'failed to update product')
            return render(request, 'products/updateproduct.html',{'forms':form})


    context={
        'forms':ProductForm(instance=instance)  #the front instance is parameter name or smth and the back one is the variable
    }
    return render(request, 'products/updateproduct.html',context)
