from django.urls import path
from .views import (
    show_profile,
    feed,
    follows_list,
    followers_list,
    follows,
    stop_follow,
    like
)

app_name = 'accounts'

urlpatterns = [
    path('', feed, name='feed'),
    path('like/', like, name='like'),
    path('<str:username>/', show_profile, name="profile"),
    path('<str:username>/followed_to', follows_list, name='follow_list'),
    path('<str:username>/followed_by', followers_list, name='followers_list'),
    path('<str:username>/follows', follows, name='follows'),
    path('<str:username>/stop_follow', stop_follow, name='stop_follow'),
]
