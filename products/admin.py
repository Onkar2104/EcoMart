from django.contrib import admin
from products.models import AddProduct
# from account.models import User

# Register your models here.


class AddProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'product_category', 'product_type', 'brand', 'user_email']
    list_display = ['product_name', 'price', 'brand', 'user_email']
    readonly_fields = ['user_email', 'user_phone'] 

    fieldsets = (
        ('Seller Info', {'fields': ('user_email', 'user_phone')}),
        ('Product Info', {'fields': ('product_name', 'product_image', 'product_image2', 'product_image3', 'product_video', 'gender', 'product_category', 'product_type', 'description', 'price', 'color', 'brand', 'discount', 'discounted_price', 'stock', 'sizes')}),
    )

    def user_email(self, obj):
        return obj.user.email

    def user_phone(self, obj):
        return obj.user.phone

admin.site.register(AddProduct, AddProductAdmin)
