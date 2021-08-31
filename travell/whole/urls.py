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
    path('maldives/', views.maldives, name="maldives"),
    path('teams/', views.teams, name="teams"),

    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('razor/', views.homepage, name='index'),
    path('success/', views.success, name='success'),
    path('deleteitem/<int:item_id>', views.deleteitem),
    path('index/', views.index, name='index'),







]


