from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.paginator import Paginator
from .models import Product, Order, Category, Supplier
from .forms import ProductForm
from django.urls import reverse_lazy

from django.contrib import messages


class HomePageListView(ListView):
    template_name = "index.html"
    model = Product
    paginate_by = 5
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        product_images = []
        for product in products:
            product_images.append(product.image.url)
        context['product_images'] = product_images
        return context
    
class ProductCreateView(CreateView):
    model = Product
    template_name = "create_product.html"
    form_class = ProductForm
    success_message = ("Successfully created product.")
    failure_message = ("Failed to create product.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        context['suppliers'] = Supplier.objects.all().order_by('name')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.failure_message)
        return super().form_invalid(form)
    
class ProductUpdateView(UpdateView):
    model = Product
    template_name = "edit_product.html"
    form_class = ProductForm
    success_message = ("Successfully updated product.")
    failure_message = ("Failed to updated product.")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.failure_message)
        return super().form_invalid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class ProductListView(ListView):
    template_name = 'product_list.html'
    paginate_by = 5
    model = Product
    context_object_name = 'products'

class OrderListView(TemplateView):
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        orders = Order.objects.all()
        paginator = Paginator(orders, 10)
        page = self.request.GET.get('page')
        orders = paginator.get_page(page)
        return {'orders': orders}
