from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name=_("user"))
    bio = models.TextField(blank=True, verbose_name=_("bio"))
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/", verbose_name=_("profile image"))
    website_url = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("website url"))
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("discussion")
