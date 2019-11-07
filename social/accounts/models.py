import os
import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import random_player_id_generator


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    followed_to = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    
    def __str__(self):
        return self.user.username

# def player_id_creation(sender, instance, *args, **kwargs):
#     if not instance.player_id:
#         instance.player_id = random_player_id_generator()

# pre_save.connect(player_id_creation, sender=Profiles)

User.profile = property(lambda u: Profiles.objects.get_or_create(user=u)[0])
