from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

from admins.models import Product, Category, Cart, OrderSummary
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm


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

def maldives(request):
    return render(request, 'whole/maldives.html')

def teams(request):
    return render(request, 'whole/team.html')

def checks(request):
    return render(request, "whole/check.html")
def success(request):
    return render(request, 'whole/success.html')

def index(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        return render(request, 'whole/email_sent.html', {'email': email})

    return render(request, 'whole/index.html', {})


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



def deleteitem(request,item_id):
    item=Cart.objects.get(id=item_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS,'Items deleted')
    return redirect('/cart')







@login_required
def addToCart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    Cart.objects.create(product=product, user=user)
    messages.add_message(request, messages.SUCCESS,'Item added to cart')
    return redirect('/cart')


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'whole/razor.html', context=context)


@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                amount = 20000  # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()# def deleteProduct(request,product_id):
#     product=Product.objects.get(id=product_id)
#     os.remove(product.image.path)
#     product.delete()
#     messages.add_message(request, messages.SUCCESS,'Product deleted')
#     return redirect('/admin-dashboard/getProduct')
#
#
#
#
# def updateProduct(request,product_id):
#     product=Product.objects.get(id=product_id)
#     if request.method=='POST':
#         form=ProductForm(request.POST,request.FILES,instance=product)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Product updated successfully')
#             return redirect('/admin-dashboard/getProduct')
#         else:
#             messages.add_message(request, messages.ERROR, 'Unable to update product')
#             return render(request, 'admins/updateProduct.html', {'form': form})
#     context={
#         'form':ProductForm(instance=product),
#         'activate_productMF':'active'
#     }
#     return render(request,'admins/updateProduct.html',context)
