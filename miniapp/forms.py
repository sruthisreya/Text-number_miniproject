from django import forms
from .models import Loguser  # Assuming the User model exists in your models.py
import re

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, label="username")
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Cpassword")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
            return email
        # if not email.endswith('@gmail.com'):
        else:
            raise forms.ValidationError("Email must be a valid Gmail address.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('Cpassword')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
