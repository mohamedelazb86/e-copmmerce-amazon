from django.urls import path
from .views import order_list,checkout

urlpatterns = [
    path('orderlist',order_list),
    path('checkout',checkout),
]
