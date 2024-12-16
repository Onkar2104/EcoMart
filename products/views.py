from django.shortcuts import render

# Create your views here.

def home_page(requests):
    context = {"page":"EcoMart"}
    return render(requests, 'index/index.html', context)

def shop(requests):
    context = {"page":"Shop"}
    return render(requests, "index/shop.html", context)

def blog(requests):
    context = {"page":"Blog"}
    return render(requests, "index/blog.html", context)

def product(requests):
    context = {"page":"Product Name"}
    return render(requests, "index/single-product-details.html", context)

def contact(requests):
    context = {"page":"Contact Us"}
    return render(requests, "index/contact.html", context)

def checkout(requests):
    context = {"page":"Payment Gateway"}
    return render(requests, 'index/checkout.html', context)