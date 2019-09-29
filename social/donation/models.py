import os
import stripe
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save


class Donation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    donation_id = models.CharField(max_length=200)
    amount = models.FloatField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


def donation_profile(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        Donation.objects.create(user=instance, email=instance.email)


post_save.connect(donation_profile, sender=User)
