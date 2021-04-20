from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('products', views.getProduct),
    path('items/<int:category_id>', views.btnplace),
    path('addToCart/<int:product_id>', views.addToCart),
    path('check/',views.cart,name="cart"),

]


