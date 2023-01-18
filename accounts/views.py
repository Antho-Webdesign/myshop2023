from django.contrib import messages
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile, Customer

User = get_user_model()


# Create your views here.
def signup(request):
    # form = UserCreationForm(request.POST)
    # context = {'form': form}
    user = request.user
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            user = Customer.objects.create_user(username, email, password)
            profile = Profile.objects.create(user=user)
            user.save()
            messages.success(request, 'Your account has been created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    return render(request, 'accounts/signup.html', {'user': user})


def login_user(request):
    user = request.user
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html', {'user': user})


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile,
    }
    if request.method == "POST":
        # traiter le formulaire
        image_profile = request.FILES.get("image_profile")
        profile.image_profile = image_profile
        profile.save()
        messages.success(request, 'Your profile has been updated successfully')
        return redirect('profile')

    return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip_code")
        state = request.POST.get("state")
        country = request.POST.get("country")

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile.phone = phone
        profile.address = address
        profile.city = city
        profile.zip_code = zip_code
        profile.state = state
        profile.country = country
        profile.save()
        return redirect('profile')

    context = {
        'profile': profile,
    }

    return render(request, 'accounts/profile_update.html', context)


def password_reset_form(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email := User.objects.get(email=email):
            # protocol = 'https'
            host = '127.0.0.1:8000/'
            link = 'accounts/password_reset/confirm/'
            send_mail('Password Reset', f'{host}{link}', ' ', [email], fail_silently=False)
            print(send_mail)
            return redirect('password_reset_form_done')

    return render(request, 'accounts/registration/password_reset_form.html')


def password_reset_form_done(request):
    return render(request, 'accounts/registration/password_reset_done.html')


def password_reset_confirm(request):
    return render(request, 'accounts/registration/password_reset_confirm.html')


def password_reset_complete(request):
    return render(request, 'accounts/registration/password_reset_complete.html')
