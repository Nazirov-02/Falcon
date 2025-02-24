# from django.db import models
#
# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from .managers import UserManager
# from django.db import models

# Create your models here.
# class User(AbstractUser):
#     username = None
#     email = models.EmailField('Email Address',unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()
#     def __str__(self):
#         return self.email





from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
