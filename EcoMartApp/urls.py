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
from account.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name="home_page"),
    path('shop/', shop, name="shop"),
    path('blog/', blog, name="blog"),
    path('product_id/', product_id, name="product_id"),
    path('my_products/', my_products, name="my_products"),
    path('add_product/', add_product, name="add_product"),
    path('contact/', contact, name="contact"),
    path('checkout/', checkout, name="checkout"),
    path('about/', about_us, name="about"),

    path('account/', account, name="account"),
    path('login/', login, name="login"),
    path('logout/', logout_page, name="logout"),
    path('register/', register, name="register"),

    path('health/', health, name="health"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
