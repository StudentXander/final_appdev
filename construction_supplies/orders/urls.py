from django.urls import path
from .views import ProductListView, OrderListView, HomePageListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('product/create/', ProductCreateView.as_view(), name='create-list'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='edit-product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete-product')

]
