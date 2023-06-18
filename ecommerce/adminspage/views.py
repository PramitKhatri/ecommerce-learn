from django.shortcuts import render,redirect
from userpage.models import *
from django.contrib.auth.decorators import login_required
from userpage.auth import admin_only

# Create your views here.

@login_required
@admin_only
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


@login_required
@admin_only
def user_order(request):
    order=Order.objects.all()

    context={
        'items':order
    }
    return render(request,'admin/order.html',context)

