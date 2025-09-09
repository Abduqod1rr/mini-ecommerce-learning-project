from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User ,AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES=[("customer", "Customer"),   # oddiy xaridor
        ("seller", "Seller"),       # mahsulot qo‘shadigan
             ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="customer")

    def __str__(self) :
        return f"{self.username} ({self.role})"