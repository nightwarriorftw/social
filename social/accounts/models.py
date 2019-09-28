from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    follow = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return self.user.username

User.user_profile = property(lambda u: Profiles.objects.get_or_create(user=u)[0])
