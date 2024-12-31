from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from .manager import *
 
# Create your models here.

class gallary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500,)
    photo =models.ImageField(upload_to="photos/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.user.username} - {self.text}'

# class CustomUser(AbstractUser):

#     username = None
#     phone_no = models.CharField(max_length=100,unique=True)
#     email = models.EmailField(unique=True)
#     user_bio = models.CharField(max_length=50)

#     USERNAME_FIELD = 'phone_no'
#     REQUIRED_FIELDS = ['email']
#     objects = usermanger()

