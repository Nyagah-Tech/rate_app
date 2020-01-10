from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    profile_pic = models.ImageField(upload_to="/profile",default = default.jpg)
    bio = HTMLField()
    updated_on = models.DateTimeField(auto_now_add=True)

# Create your models here.
