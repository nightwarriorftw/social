from django.urls import path
from . import views


app_name = 'donation'

urlpatterns = [
    path('', views.Donation.as_view(), name='donation'),
    path('charge/', views.charge, name='charge'),
]
