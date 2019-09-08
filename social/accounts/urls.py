from django.urls import path
from .views import (
    show_profile,
    feed
)


app_name= 'accounts'

urlpatterns = [
    path('', feed, name='feed'),
    path('<str:username>/', show_profile, name="profile"),
]
