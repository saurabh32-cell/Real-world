from django import forms
from .models import *
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"


class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields="__all__"

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields="__all__"


