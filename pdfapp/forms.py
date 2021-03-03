from django import forms
from .models import BookSearch
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchBookForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {
        "class": "form-control me-2", "placeholder": "Enter book name",
    }))

    class Meta:
        model = BookSearch
        fields = ['name',]

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "Enter Username",
    }))
    email = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "Enter Email",
    }))
    password1 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs = {
        "class": "form-control", "placeholder": "At least eight characters",
    }))
    password2 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs = {
        "class": "form-control", "placeholder": "Confirm password",
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']