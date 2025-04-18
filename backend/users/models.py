from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
class User(AbstractUser):
    username = None  # Remove username field
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)  # Make email required + unique

    # USERNAME_FIELD tells Django what field to use for login
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS are required when creating superusers via CLI
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email