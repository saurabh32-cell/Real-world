from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from admins.models import Product, Category, Cart, OrderSummary


def store(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context={
        'products': products,
        'categories':categories
    }
    return render(request, 'whole/store.html',context)


def btnplace(request, category_id):
    categories = Category.objects.get(id=category_id)
    products = Product.objects.filter(category_id=categories)
    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'whole/items.html',context)


def aboutPage(request):
    return render(request, 'SafalYatra/about.html')

@login_required
def cart(request):
    items = Cart.objects.filter(user=request.user)
    context={
        'items':items
    }
    return render(request, 'whole/cart.html',context)


def checkout(request):
    items = Cart.objects.filter(user=request.user)
    context = {
        'items': items
    }
    return render(request, 'whole/checkout.html',context)

def getProduct(request):
    products= Product.objects.all().order_by('-id')
    context={
        'products': products,
        'activate_serviceMF':'active'
    }
    return render(request, 'whole/products.html',context)

def addToCart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    Cart.objects.create(product=product, user=user)
    messages.add_message(request, messages.SUCCESS,'Item added to cart')
    return redirect('/cart')

def Check(request):
    return render(request, 'whole/check.html')
