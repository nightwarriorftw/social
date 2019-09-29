import os
import stripe
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Donation
from django.contrib.auth.decorators import login_required

stripe_pub_key = os.environ["stripe_public_key"]
stripe_api_key = os.environ["stripe_api_key"]


@login_required
def donation_payment(request):
    if request.method == "POST":
        token = request.POST["stripeToken"]
        amount = request.POST["amount"]
        print(token)
        print(amount)
        stripe.api_key = os.environ["stripe_api_key"]
        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            source=token,
        )
        Donation.objects.create(
            user=request.user, email=request.user.email, donation_id=charge.id, amount=amount)

        print(charge)
    return render(request, 'donation/payment.html', {"public_key": stripe_pub_key})
