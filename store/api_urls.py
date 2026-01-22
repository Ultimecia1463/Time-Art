from django.urls import path
from . import api_views

urlpatterns = [
    path('products/', api_views.product_list_api),
    path('orders/', api_views.order_history_api),
]
