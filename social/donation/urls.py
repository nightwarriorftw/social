from django.urls import path
from .views import donation_payment

app_name = "donation"

urlpatterns = [
    path('', donation_payment, name="donation"),
    # path('donation/card', payment_method_create_view, name="card"),
]
