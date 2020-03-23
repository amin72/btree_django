from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib import auth
from contacts.models import Contact


User = get_user_model()



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            return redirect('accounts:dashboard')
        
        # user can't login, wrong credentials or not active user
        messages.error(request, "Invalid credentials")
    context = {
        'login_active': True
    }
    return render(request, 'accounts/login.html', context)



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are logged out")
        return redirect('pages:index')
    


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "That email is being used")
            else:
                user = User.objects.create_user(username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name)
                messages.success(request, "You are now registered and can log in")
                return redirect('accounts:login')
        else:
            messages.error(request, "Passwords do not match")

    context = {
        'register_active': True
    }
    return render(request, 'accounts/register.html', context)



def dashboard(request):
    inquiries = Contact.objects.filter(user_id=request.user.id) \
        .order_by('-contact_date')

    context = {
        'inquiries': inquiries,
        'dashboard_active': True
    }
    return render(request, 'accounts/dashboard.html', context)
