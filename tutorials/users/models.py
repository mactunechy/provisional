from django.contrib.auth.models import AbstractUser
from django.db import models

from memberships.models import Membership

class CustomUser(AbstractUser):
    subscription = models.ForeignKey(Membership,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.email
