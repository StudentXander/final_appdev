from django.urls import path
from .views import ProductListView, OrderListView, HomePageListView

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]
