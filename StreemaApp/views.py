from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login as lg, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from StreemaApp.forms import ContactForm


# -------------------------------------------------------------------------

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            user = authenticate(request=request, username=email, password=password)
            if user:
                lg(request, user)
                return redirect('/home/')
            else:
                messages.error(request, "Invalid Credentials!")
                return redirect('/login/')
        else:
            messages.error(request, "Email and password are required.")
            return redirect('/login/')
    return render(request, 'Pages/login.html')

@login_required
def movies(request):
    return render(request, 'Pages/movies.html')

@login_required
def series(request):
    return render(request, 'Pages/series.html')

# @login_required
# def contact (request):
#     if request.method == 'POST':
#         form = contact(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         return render(request, 'Pages/Contact.html')

@login_required
def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'Pages/Contact.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_emp(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    if email and password:
        user = authenticate(request=request, username=email, password=password)
        if user:
            login(request=request, user=user)
            return redirect('home/')
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('login/')
    else:
        messages.error(request, "Email and password are required.")
        return redirect('login/')


def view_create_page(request):
    return render(request, 'Pages/register.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        messages.success(request, "User created successfully!")
        return redirect('login')
    return render(request, 'Pages/register.html')

@login_required
def FreeGuy(request):
    return render(request, 'All Movies and Shows/FreeGuy.html')

@login_required
def Joker(request):
    return render(request, 'All Movies and Shows/Joker.html')

@login_required
def BossBaby(request):
    return render(request, 'All Movies and Shows/BabyBoss.html')
