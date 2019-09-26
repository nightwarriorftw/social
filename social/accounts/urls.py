from django.urls import path
from .views import (
    show_profile,
    feed,
    follow, 
    followers,
    follows,
    stop_follow
)

app_name= 'accounts'

urlpatterns = [
    path('', feed, name='feed'),
    path('<str:username>/', show_profile, name="profile"),
    path('<str:username>/follow', follow, name='follow'),
    path('<str:username>/followers', followed, name='followed'),
    path('<str:username>/follows', follows, name='follows'),
    path('<str:username>/stop_follow', stop_follow, name='stop_follow')
]
