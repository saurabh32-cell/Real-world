# from django.shortcuts import render,redirect
# from .models import *
# from .forms import *
from django.contrib import messages
#
# from django.contrib.auth.decorators import login_required
import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
# from whole.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *


# Create your views here.
@login_required
@admin_only
def addCategory(request):
    if request.method == "POST":
        form= CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Category added successfully')
            return redirect('/admin-dashboard/getCategory')
        else:
            messages.add_message(request, messages.ERROR,'Unable to add service')
            return render(request, 'admins/addCategory.html',{'form':form})
    context={
        'form':CategoryForm,
        'activate_categoryMF': 'active'
    }
    return render(request,'admins/addCategory.html',context)


@login_required
@admin_only
def getCategory(request):
    categories= Category.objects.all().order_by('-id')
    context={
        'categories': categories,
        'activate_serviceMF':'active'
    }
    return render(request, 'admins/getCategory.html',context)


@login_required
@admin_only
def deleteCategory(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS,'Category deleted')
    return redirect('/admin-dashboard/getCategory')


@login_required
@admin_only
def updateCategory(request,category_id):
    category=Category.objects.get(id=category_id)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect('/admin-dashboard/getCategory')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update category')
            return render(request, 'admins/updateCategory.html', {'form': form})
    context={
        'form':CategoryForm(instance=category),
        'activate_shoesMF':'active'
    }
    return render(request,'admins/updateCategory.html',context)


@login_required
@admin_only
def addProduct(request):
    if request.method == "POST":
        form= ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Product added successfully')
            return redirect('/admin-dashboard/getProduct')
        else:
            messages.add_message(request, messages.ERROR,'Unable to add product')
            return render(request, 'admins/addProduct.html',{'form':form})
    context={
        'form':ProductForm,
        'activate_productMF': 'active'
    }
    return render(request,'admins/addProduct.html',context)


@login_required
@admin_only
def getProduct(request):
    products= Product.objects.all().order_by('-id')
    context={
        'products': products,
        'activate_productMF':'active'
    }
    return render(request, 'admins/getProduct.html',context)


@login_required
@admin_only
def deleteProduct(request,product_id):
    product=Product.objects.get(id=product_id)
    os.remove(product.image.path)
    product.delete()
    messages.add_message(request, messages.SUCCESS,'Product deleted')
    return redirect('/admin-dashboard/getProduct')


@login_required
@admin_only
def updateProduct(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product updated successfully')
            return redirect('/admin-dashboard/getProduct')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update product')
            return render(request, 'admins/updateProduct.html', {'form': form})
    context={
        'form':ProductForm(instance=product),
        'activate_productMF':'active'
    }
    return render(request,'admins/updateProduct.html',context)



@login_required
@admin_only
def admin_dashboard(request):

    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {

        'user': user_count,
        'admin': admin_count
    }
    return render(request, 'admins/adminDashboard.html', context)
@login_required
@admin_only
def get_user(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users':users,
    }
    return render(request,'admins/showUser.html',context)

@login_required
@admin_only
def update_user_to_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS,
                         'User has been updated to Admin')
    return redirect('/admin-dashboard')

@login_required
@admin_only
def register_user_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'User Registered Successfully')
            return redirect('/admin-dashboard')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please provide correct details')
            return render(request, "admins/register-user-admin.html", {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'admins/register-user-admin.html', context)

