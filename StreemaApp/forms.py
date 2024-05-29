from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
from django import forms
from .models import Contact

# class signup(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'email', 'phone', 'message']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # model = User
        fields = ['email', 'password', 'password2']