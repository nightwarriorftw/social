from django import forms
from django.contrib.auth.models import User



class SignInForm(forms.Form):

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"class": "input-details", "placeholder": "Username"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "input-details", "placeholder": "Password"}))


class SignUpForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True)
    user_name = forms.CharField(required=True, max_length=250)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =('first_name',
                   'last_name',
                   'user_name',
                   'email',
                   'password1',
                   'password2'
                )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("Username is taken")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Confirmation password is not correct")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.firstname=self.cleaned_data['first_name']
        user.lastname=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['user_name']

        if commit:

            user.save()
        
        return user
