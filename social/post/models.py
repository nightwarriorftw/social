import os
import random
from django.db import models
from django.contrib.auth.models import User


def file_name(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splittext(basename)
    return name, ext

def image_upload(instance, filename):
    name, ext = get_name(file_name)
    secondaryName = random.randint(100000)
    finalName = "{name}{secondaryName}".format(name=name, secondaryName=secondaryName)
    imageName = "{finalName}{ext}".format(finalName=finalName, ext=ext)
    return "/instance/posts/image/{imageName}".format(imageName=imageName)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=50)
    image = models.ImageField(upload_to=image_upload, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.user.first_name
