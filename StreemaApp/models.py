from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # Add any additional fields here
#     pass

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=65)
    phone = models.IntegerField()

# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser

# python manage.py runserver
# from django.db import models

# Create your models here.
