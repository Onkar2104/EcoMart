from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

User = get_user_model()


def login(request):
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            messages.info(request, "Invalid Email.!")
            print
            return redirect('/login/')

        user = authenticate(request, email = email, password = password)

        if User is None:
            messages.info(request, "Create Account First.!")
            return redirect('/login/')
        else:
            auth_login(request, user)
            return redirect('/')

        
    context = {"page": "Login"}
    return render(request, "login_page.html", context)

def logout(request):
    logout(request)
    return redirect(' /')

def register(request):

#     profile = User.objects.get_or_create(user=user)

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         middle_name = request.POST.get('middle_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email').lower()
#         phone = request.POST.get('phone')

#         if not 

    context = {"page": "Register"}
    return render(request, "register.html", context)