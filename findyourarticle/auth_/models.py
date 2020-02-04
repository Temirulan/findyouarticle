from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.template.loader import render_to_string
from django.utils import timezone

from datetime import timedelta
import random
import string


class MainUserManager(BaseUserManager):
    """
    Main user manager
    """

    def create_user(self, email=None, password=None):
        """
        Creates and saves a user with the given email.
        """
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given phone and password
        """
        user = self.model(email=email)
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MainUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    full_name = models.CharField(max_length=555,
                                 blank=False,
                                 null=True,
                                 verbose_name='Full name')
    email = models.EmailField(max_length=50,
                              blank=True,
                              null=True,
                              db_index=True,
                              unique=True,
                              verbose_name='Email')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    objects = MainUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return '{}'.format(self.full_name)
