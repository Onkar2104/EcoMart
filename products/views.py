from django.shortcuts import render
from products.models import AddProduct
from account.models import User
from django.contrib import messages

# Create your views here.

def home_page(request):
    context = {"page":"EcoMart"}
    return render(request, 'index/index.html', context)

def shop(request):
    context = {"page":"Shop"}
    return render(request, "index/shop.html", context)

def my_products(request):
    user = request.user

    context = {'page':'My_Products'}
    return render(request, 'index/my_products.html', context)

def add_product(request):
    user = request.user
    # email = User.email

    # product = AddProduct.objects.get()

    if request.method =='POST':
        product = AddProduct(
            user = user, 
            product_name = request.POST.get('product_name'),
            gender = request.POST.get('gender'),
            product_category = request.POST.get('product_category'),
            product_type = request.POST.get('product_type'),
            description = request.POST.get('description'),
            price = request.POST.get('price'),
            color = request.POST.get('color'),
            brand = request.POST.get('brand'),
            discount = request.POST.get('discount'),
            discounted_price = request.POST.get('discounted_price'),
            stock = request.POST.get('stock'),
            sizes = request.POST.get('sizes'),
            product_image = request.FILES.get('product_image'),
            product_image2 = request.FILES.get('product_image2'),
            product_image3 = request.FILES.get('product_image3'),
            product_video = request.FILES.get('product_video'),
        )

        product.save()

        messages.success(request, "Product saved successfully.!")
        print("Product Added successfully.")

    context = {
        'page': 'Add Product',
        # 'product_name': product_name,
        # 'gender': gender,
        # 'product_category': product_category,
        # 'product_type': product_type,
        # 'description': description,
        # 'price':price,
        # 'color': color,
        # 'brand': brand,
        # 'discount': discount,
        # 'discounted_price': discounted_price,
        # 'stock': stock,
        # 'available_stock': available_stock,
        # 'sizes': sizes,
        # 'product_image': product_image,
        # 'product_video': product_video,
        }

    return render(request, 'index/add_product.html', context)

def blog(request):
    context = {"page":"Blog"}
    return render(request, "index/blog.html", context)

def product(request):
    context = {"page":"Product Name"}
    return render(request, "index/single-product-details.html", context)

def contact(request):
    context = {"page":"Contact Us"}
    return render(request, "index/contact.html", context)

def checkout(request):
    context = {"page":"Payment Gateway"}
    return render(request, 'index/checkout.html', context)

def about_us(request):
    context = {'page':'About Us'}
    return render(request, "index/regular-page.html", context)