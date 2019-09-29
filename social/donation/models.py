import os
import stripe
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_id = models.CharField(max_length=200)

    def __str__(self):
        return "{username}||{email}".format(username=self.user.username, email=self.user.email)


stripe.api_key = os.environ['stripe_api_key']


def stripe_customer_creation(sender, instance, *args, **kwargs):
    if not instance.user_id and instance.email:

        instance.donation_id = strip.Customer.create(email=instance.email).id


pre_save.connect(stripe_customer_creation, sender=Donation)


def donation_profile(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        Donation.objects.create(user=instance, email=instance.email)


post_save.connect(donation_profile, sender=User)
