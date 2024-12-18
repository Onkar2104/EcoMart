from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import random
from account.models import User, Account
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


@login_required(login_url="/login/")
def account(request):

    
    # account_update = User.objects.get(user=request.user)

    try:
        # profile = User.objects.get(user=request.user)
        account = Account.objects.get(user=request.user)

        first_name = request.user.first_name
        middle_name = request.user.middle_name
        last_name = request.user.last_name
        email = request.user.email
        phone = request.user.phone

        if account.date_of_birth:
            date_of_birth = account.date_of_birth.strftime('%Y-%m-%d')
        else:
            date_of_birth = ''

        profile_image = account.profile_image
        # date_of_birth = account.date_of_birth
        gender = account.gender
        address = account.address
        land_mark = account.land_mark
        city = account.city
        state = account.state
        country = account.country
        postal_code = account.postal_code

    except Account.DoesNotExist:
        account = Account(user=request.user)

        first_name = request.user.first_name if request.user.first_name else ""
        middle_name = getattr(request.user, 'middle_name', "")
        last_name = request.user.last_name if request.user.last_name else ""
        email = request.user.email if request.user.email else ""
        phone = getattr(request.user, 'phone', "")
        
        profile_image = account.profile_image if account.profile_image else ""
        date_of_birth = account.date_of_birth if account.date_of_birth else ""
        gender = account.gender if account.gender else ""
        address = account.address if account.address else ""
        land_mark = account.land_mark if account.land_mark else ""
        city = account.city if account.city else ""
        state = account.state if account.state else ""
        country = account.country if account.country else ""
        postal_code = account.postal_code if account.postal_code else ""

        if request.method == "POST":
            account.profile_image = request.FILE.get('profile_image') if request.FILES.get('profile_image') else account.profile_image
            account.date_of_birth = request.POST.get('date_of_birth')
            account.gender = request.POST.get('gender')
            account.address = request.POST.get('address')
            account.land_mark = request.POST.get('land_mark')
            account.city = request.POST.get('city')
            account.state = request.POST.get('state')
            account.country = request.POST.get('country')
            account.postal_code = request.POST.get('postal_code')

            account.save()
            messages.success(request, "Profile updated successfully.!")
            return redirect('/account/')
        

    ### For Update account data ###
    update_user = request.user
    update_account = Account.objects.get(user = request.user)

    if request.method == "POST":
        update_user.first_name = request.POST.get('first_name', update_user.first_name)
        update_user.middle_name = request.POST.get('middle_name')
        update_user.last_name = request.POST.get('last_name')
        update_user.phone = request.POST.get('phone')

        update_account.profile_image = request.FILES.get('profile_image') if request.FILES.get('profile_image') else update_account.profile_image
        update_account.date_of_birth = request.POST.get('date_of_birth')
        update_account.gender = request.POST.get('gender')
        update_account.address = request.POST.get('address')
        update_account.land_mark = request.POST.get('land_mark')
        update_account.city = request.POST.get('city')
        update_account.state = request.POST.get('state')
        update_account.country = request.POST.get('country')
        update_account.postal_code = request.POST.get('postal_code')

        update_user.save()
        update_account.save()
        

        messages.success(request, "Updated Successfully.!")
        return redirect('/account/')



    context = {
        "page":"My Account",
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'profile_image': profile_image,
        'date_of_birth': date_of_birth,
        'gender': gender,
        'address': address,
        'land_mark': land_mark,
        'city': city,
        'state': state,
        'country': country,
        'postal_code': postal_code,
        }
    
    return render(request, "account.html", context)