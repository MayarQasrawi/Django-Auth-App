from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model which extends Django's built-in AbstractUser.

    Key points:
    1. We add a unique email field to use email for authentication instead of username.
    2. USERNAME_FIELD = "email" tells Django to use the email field as the login identifier.
    3. REQUIRED_FIELDS = ["username"] ensures that the username is still required when creating a user via createsuperuser.
    4. __str__ method returns the email when printing the user object.
    """
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "username"       
    REQUIRED_FIELDS = ["email"]  # email still required


    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.email}"
