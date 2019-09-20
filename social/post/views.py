from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators login_required


@login_required
def profile(request, username):
    user = 
    


