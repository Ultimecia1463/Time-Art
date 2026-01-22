from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_history, name='orders'),


]
