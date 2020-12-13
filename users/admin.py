from django.contrib import admin

# Register your models here.
from .models import Profile #this to register our profile model with the admin file for our so that we can see this in our admin page 

admin.site.register(Profile)
