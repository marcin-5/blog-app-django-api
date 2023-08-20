from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.utils import base64uuid

from .managers import CustomUserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    pk_id = models.BigAutoField(primary_key=True, editable=False)
    id = models.CharField(
        default=base64uuid(fixed_length=22),
        max_length=22,
        validators=(MinLengthValidator(22),),
        editable=False,
        unique=True,
    )
    email = models.EmailField(
        verbose_name=_("email address"), db_index=True, unique=True, max_length=60
    )

    objects = CustomUserManager()
