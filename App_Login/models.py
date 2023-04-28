from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics')