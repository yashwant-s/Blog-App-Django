from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile

#here we are creating a receiver function to add an instance to the Profile model whenever a user is created
@receiver(post_save, sender=User)#here we are adding receiver decorator and whenevr a user is added to the User it sends a signal to the receiver function 
def create_profile(sender, instance, created, **kwargs):
      if created:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
      instance.profile.save()