import stripe
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

class Donation(TemplateView):
    template_name = 'donation/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context

@login_required
def charge(request):
    if request.method == "POST":

        charge = stripe.Charge.create(
            amount = 100,
            currency = 'usd',
            source = request.POST["stripeToken"],
            description = "donation from {donator}".format(donator=request.POST["stripeEmail"])            
        )
        return render(request, "donation/charge.html", {})
