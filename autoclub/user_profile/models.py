from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE, null=True, db_index=True)
    bio = models.TextField(_("bio"), blank=True)
    profile_pic = models.ImageField(_("profile image"), upload_to='images/profile/', null=True, blank=True)
    website_url = models.CharField(_("website url"), max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"pk": self.pk})
