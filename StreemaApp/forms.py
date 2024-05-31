from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'email', 'phone', 'message']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

class signup(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')