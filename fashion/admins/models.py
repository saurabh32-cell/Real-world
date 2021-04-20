
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, unique=True)
    image = models.ImageField(upload_to='static/uploads', blank=False, null=True)
    created_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name

class Product(models.Model):
    name=models.CharField(max_length=100, null=True)
    price= models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=2000)
    image=models.ImageField(upload_to='static/uploads', blank=False , null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product


class OrderSummary(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product
