from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Supplier(BaseModel):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    def get_absolute_url(self):
        return reverse('product_list')


    def __str__(self):
        return self.name
    

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order by {self.user.username}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
