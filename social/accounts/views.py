from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .forms import SignInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect(reverse('accounts:feed'))
    return render(request, 'social/home.html', {})


def auth_login(request):

    if request.method=="POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('accounts:feed'))
        
    else:
        form=SignInForm(None)
        
    context={
        "signinform": form
    }
    return render(request, 'auth/login.html', context)



def auth_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method=="POST":
        if "signupform" in request.POST:
            form=SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Signed In')
                print('User created')
                return redirect('/')
            else:
                messages.error(request, "Internal Server Error")
                return redirect("{% url 'accounts:register' %}")
        
        else:
            return redirect("/")
    else:
        form=SignUpForm(None)
    
    context = {
        "signupform": form 
    }

    return render(request, "auth/register.html", context)


@login_required
def auth_logout(request):
    logout(request)
    return redirect('/')


def show_profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

    else:
        user=None
        return redirect("{% url 'accounts:login' %}")

    return render(request, 'profile/user.html', {"user": user})


def feed(request):
    username = request.user.username
    user = User.objects.get(username=username)
    context = {
        "user": user
    }
    return render(request, "social/feed.html", context)
