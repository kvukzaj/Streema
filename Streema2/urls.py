"""
URL configuration for Streema2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from StreemaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='home'),
    path('home/', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('contact/', views.contact, name='contact'),
    path('FreeGuy', views.FreeGuy, name='freeguy'),
    path('Joker', views.Joker, name='joker'),
    path('BossBaby', views.BossBaby, name='bossbaby')
]