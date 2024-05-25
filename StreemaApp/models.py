from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     # Add any additional fields here
#     pass

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=65)
    phone = models.IntegerField()


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser

# python manage.py runserver
# from django.db import models

# Create your models here.
