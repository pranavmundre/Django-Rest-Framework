from django.contrib.auth.models import AbstractUser
from django.db import models

from account.manager import UserManager
from account.validations import only_int


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, )
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=3, null=True, blank=False, default='+91',)
    mobile_no = models.CharField(max_length=10, unique=True, null=True, blank=False, validators=[only_int])

    objects = UserManager()

    is_verified = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
