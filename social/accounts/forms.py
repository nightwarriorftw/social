from django import forms
from django.contrib.auth.models import User

class SignInForm(forms.Form):
    
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

class SignUpForm(forms.ModelForm):

    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    passwordagain = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password Again}))

    class Meta:
        model=User
        fields = ['firstname', 'lastname', 'username', 'email', 'password', 'passwordagain']
