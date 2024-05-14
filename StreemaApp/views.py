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

@login_required
def contact (request):
#     if request.method == 'POST':
#         firstname = request.POST.get('firstname')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
#     else:
        return render(request, 'Pages/Contact.html')

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
    User.objects.create(
        email=request.POST.get("email"),
        password=request.POST.get("password"),
    )
    messages.success(request, "User Created Successfully!")


@login_required
def FreeGuy(request):
    return render(request, 'All Movies and Shows/FreeGuy.html')

@login_required
def Joker(request):
    return render(request, 'All Movies and Shows/Joker.html')

@login_required
def BossBaby(request):
    return render(request, 'All Movies and Shows/BabyBoss.html')
