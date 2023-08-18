from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        validators=[AbstractUser.username_validator],
        error_messages=({"unique": _("A user with that username already exists.")}),
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
