from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from pages.models import Page

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Logged in successfully."))
            return redirect('login')
        else:
            messages.success(request, ("Issue loggin in, try again..."))
            return redirect('login')
    else:
        page_list = Page.objects.all()
        return render(request, 'authentication/login.html', {"page_list": page_list})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out successfully."))
    return redirect('login')

def register_user(request):
    page_list = Page.objects.all()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registered successfully."))
            return redirect('register_user')
    else:
        form = RegisterUserForm()
    
    return render(request, 'authentication/register_user.html', {"page_list": page_list, 'form': form})

