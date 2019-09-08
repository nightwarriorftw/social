from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignInForm(forms.Form):

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password"}))


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)
    user_name = forms.CharField(required=True, max_length=250)

    class Meta:
        model = User
        fields =('first_name',
                   'last_name',
                   'user_name',
                   'email',
                   'password1',
                   'password2'
                )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.firstname=self.cleaned_data['first_name']
        user.lastname=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['user_name']

        if commit:

            user.save()
        
        return user
    
