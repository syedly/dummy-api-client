from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='in stock')
    category = models.CharField(max_length=50, null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class purchase(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.IntegerField()
    purchase_month = models.CharField(max_length=20)
    purchase_year = models.IntegerField()
    province = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    last_digits = models.CharField(max_length=4, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Purchase of {self.product.name} on {self.purchase_date}"