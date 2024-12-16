"""
URL configuration for EcoMart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('shop/', shop, name="shop"),
    path('blog/', blog, name="blog"),
    path('product_id/', product, name="product"),
    path('contact/', contact, name="contact"),
    path('checkout/', checkout, name="checkout"),

    path('admin/', admin.site.urls),
]
