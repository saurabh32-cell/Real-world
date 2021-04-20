from django.urls import path
from . import views

urlpatterns = [
    path('addCategory', views.addCategory),
    path('getCategory', views.getCategory),
    path('deleteCategory/<int:category_id>',views.deleteCategory),
    path('updateCategory/<int:category_id>',views.updateCategory),

    path('addProduct', views.addProduct),
    path('getProduct', views.getProduct),
    path('deleteProduct/<int:product_id>',views.deleteProduct),
    path('updateProduct/<int:product_id>',views.updateProduct),


    path('',views.admin_dashboard),
    path('show-user',views.get_user),
    path('update-user-to-admin/<int:user_id>',views.update_user_to_admin),
    path('register-user', views.register_user_admin),
    #
    # path('addProduct', views.addProduct),
    # path('getProduct', views.getProduct),
    # path('deleteProduct/<int:product_id>', views.deleteProduct),
    # path('updateProduct/<int:product_id>', views.updateProduct),

]