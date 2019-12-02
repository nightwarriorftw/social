import json
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .forms import SignInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.forms import AddPost
from post.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .utils import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse, Http404

from django.views.generic import DetailView

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect(reverse('accounts:feed'))
    return render(request, 'social/home.html', {})


def auth_login(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect(reverse('accounts:feed'))

    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('accounts:feed'))
            else:
                messages.error(request, "Invalid username/password")
                return redirect(reverse('login'))
    else:
        form = SignInForm(None)

    context = {
        "signinform": form
    }
    return render(request, 'auth/login.html', context)


def auth_register(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect(reverse('accounts:feed'))

    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Social account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.info(
                request, "Please confirm your Email address to complete the registration")
            return redirect(reverse('register'))

    else:
        form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, "auth/register.html", context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, User.DoesNotExist, ValueError, OverflowError):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank You for confirming. You can now login.')
    else:
        return HttpResponse('Activation link is invalid')


@login_required(login_url="/login/")
def auth_logout(request):
    logout(request)
    return redirect('/login')


@login_required(login_url="/login/")
def show_profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        post = Post.objects.filter(user=user)
        context = {
            "user": user,
            "post": post
        }
    return render(request, 'profile/user.html', context)


@login_required(login_url="/login/")
def feed(request):

    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.body = form.cleaned_data['body']
            if form.cleaned_data['image']:
                instance.image = form.cleaned_data['image']
            instance.save()
            return redirect(reverse("accounts:feed"))

    else:
        form = AddPost()

    username = request.user.username
    user = get_object_or_404(User, username=username)


    # Implementation of seeing posts of the gamers one user follow
    userId = []
    follow_list = request.user.profile.followed_to.all()

    for profiles in follow_list:
        userId.append(profiles.user_id)

    userId.append(request.user.id)

    post = Post.objects.filter(Q(user_id__in=userId)).order_by('-created_at')

    context = {
        "user": user,
        "post": post,
        "form": form,
    }

    return render(request, "social/feed.html", context)


@login_required(login_url='login')
def PostDetails(request, id):
    post = get_object_or_404(Post, pk=id)
    isLiked = False
    if post.likes.filter(id=request.user.id).exists():
        isLiked = True
    context = {
        "post": post,
        "isLiked": isLiked,
        "totalLikes": post.likes.count()
    }
    if request.is_ajax():
        html = render_to_string("snippets/likePost.html",
                                context, request=request)
        return JsonResponse({"form": html})
    return render(request, "social/post.html", context)


@login_required(login_url='login')
def postLikeToggle(request):
    isLiked = False
    post = get_object_or_404(Post, pk=request.POST.get('id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        isLiked = False
        print(post.likes.all())
    else:
        post.likes.add(request.user)
        isLiked = True
        print(post.likes.all())

    return redirect(post.get_absolute_url())


@login_required(login_url="/login/")
def follows_list(request, username):
    user = User.objects.get(username=username)
    followed_to = user.profile.followed_to.all()
    return render(request, 'profile/follow_list.html', {"user": followed_to})


@login_required(login_url="/login/")
def followers_list(request, username):
    user = User.objects.get(username=username)
    followed_by = user.profile.followed_by.all()
    return render(request, 'profile/followers_list.html', {"user": followed_by})


@login_required(login_url="/login/")
def follows(request, username):
    user = User.objects.get(username=username)
    request.user.profile.followed_to.add(user.profile)
    return redirect(reverse("accounts:profile", kwargs={"username": username}))


@login_required(login_url="/login/")
def stop_follow(request, username):
    user = User.objects.get(username=username)
    request.user.profile.followed_to.remove(user.profile)
    return redirect(reverse("accounts:profile", kwargs={"username": username}))
