from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=User)
def sync_user_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, 'profile'):
        models.Profile.objects.create(user=instance)
    else:
        instance.profile.save()
        