from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView


from django.core.paginator import Paginator
from .models import Product, Order

class HomePageListView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = 'products '

class ProductListView(TemplateView):
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        paginator = Paginator(products, 10)
        page = self.request.GET.get('page')
        products = paginator.get_page(page)
        return {'products': products}

class OrderListView(TemplateView):
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        orders = Order.objects.all()
        paginator = Paginator(orders, 10)
        page = self.request.GET.get('page')
        orders = paginator.get_page(page)
        return {'orders': orders}
