from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import random
from account.models import User
from django.core.mail import send_mail
from django.conf import settings

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

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        # Step 1: Generate and Send OTP
        if 'send_otp' in request.POST:
            # Collect user input
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email').lower()
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            # Validation
            if not email:
                messages.error(request, "Email is required.")
                print("Email is required.")
                return redirect('/register/')
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                print("Passwords do not match.")
                return redirect('/register/')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already in use.")
                print( "Email is already in use.")
                return redirect('/register/')
            try:
                validate_password(password)
            except ValidationError as e:
                messages.error(request, " ".join(e.messages))
                print("password validation")
                return redirect('/register/')

            # Generate OTP and store in session
            send_otp = random.randint(1000, 9999)
            request.session['otp'] = send_otp
            request.session['register_data'] = {
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'password': password,
            }

            # Send email with OTP
            subject = "Your Verification Code"
            message = f"Dear {first_name},\n\nYour verification code for EcoMart is: {send_otp}\n\nThank You!"
            from_mail = settings.EMAIL_HOST_USER
            recipient_list = [email]

            try:
                send_mail(subject, message, from_mail, recipient_list)
                messages.success(request, "Verification code has been sent to your email.")
                print("Verification code has been sent to your email.")
            except Exception as e:
                messages.error(request, f"Failed to send OTP: {e}")
                print("Failed")
                return redirect('/register/')

            # Prompt for OTP input
            return render(request, "register.html", {"step": "verify_otp"})

        # Step 2: Validate OTP and Create User
        elif 'verify_otp' in request.POST:
            otp_input = request.POST.get('otp')
            stored_otp = request.session.get('otp')
            register_data = request.session.get('register_data')

            if not register_data or not stored_otp:
                messages.error(request, "Session expired. Please try again.")
                print("Session expired. Please try again.")
                return redirect('/register/')

            if str(otp_input) == str(stored_otp):
                # OTP is correct, create the user
                user = User.objects.create_user(
                    first_name=register_data['first_name'],
                    middle_name=register_data['middle_name'],
                    last_name=register_data['last_name'],
                    email=register_data['email'],
                    phone=register_data['phone'],
                    password=register_data['password']
                )
                # Clear session data
                del request.session['otp']
                del request.session['register_data']

                messages.success(request, "Registration successful! Please log in.")
                print("Registration successful! Please log in.")
                return redirect('/login/')
            else:
                messages.error(request, "Invalid OTP. Please try again.")
                print("Invalid OTP. Please try again.")
                return render(request, "register.html", {"step": "verify_otp"})

    # Default: Show registration form
    return render(request, "register.html", {"step": "register"})