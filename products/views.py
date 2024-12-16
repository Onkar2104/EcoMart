from django.shortcuts import render

# Create your views here.

def home_page(request):
    context = {"page":"EcoMart"}
    return render(request, 'index/index.html', context)

def shop(request):
    context = {"page":"Shop"}
    return render(request, "index/shop.html", context)

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