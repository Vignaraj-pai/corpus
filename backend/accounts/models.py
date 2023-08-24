from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDERS = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
    ("N", "Prefer to not disclose")
]

class User(AbstractUser):
    gender = models.CharField(max_length=1, choices=GENDERS, blank=False, null=False)
    phone_no = models.CharField(max_length=13, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"