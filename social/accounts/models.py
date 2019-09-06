from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    follow = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)


def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        user_profile = Profiles.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
