from django.db import models
from django.conf import settings
from account.models import User
import uuid

# Create your models here.


class AddProduct(models.Model):
    GENDER_CHOICE = {
        ('Men','Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
        ('Unisex', 'Unisex'),
    }

    CATEGORY_CHOICE = {
        ('Clothing', 'Clothing'),
        ('Shoes', 'Shoes'),
        ('Accessories', 'Accessories'),
        ('Watch', 'Watch')
    }

    BRAND_CHOICE = {
        ('Zara', 'Zara'),
        ('Asos', 'Asos'),
        ('River', 'River'),
        ('Titan', 'Titan'),
    }

    PRODUCT_CHOICE = {
        ('Casual', 'Casual'),
        ('Sports', 'Sports'),
        ('Business_casual', 'Business_casual'),
        ('Wedding', 'Wedding'),
        ('Formal', 'Formal'),
        ('Kurtas', 'Kurtas'),
    }

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    product_category = models.CharField(max_length=30, choices=CATEGORY_CHOICE)
    product_type = models.CharField(max_length=20, choices=PRODUCT_CHOICE)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=False, blank=False, default='1000')
    color = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, choices=BRAND_CHOICE)
    discount = models.FloatField(blank=True, null=True)
    discounted_price = models.FloatField(blank=True, null=True, default='0')
    stock = models.IntegerField(blank=False, null=False, default='10')
    # available_stock = models.IntegerField()
    sizes = models.CharField(max_length=5)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    product_video = models.FileField(upload_to='products/', null=True, blank=True)
    # shipping_price = models.IntegerField(blank=True, null=True, default='40')

    def __str__(self):
        return self.product_name
    
    def __str__(self):
        return self.user.email