from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .formatchecker import ContentTypeRestrictedFileField
from .choices import PROVIDER, REGION_CHOICES, USER_GENDER

phone_regex = RegexValidator(
    regex=r"^(\+996),?\s?\d{9}$",
    message="Phone number must be entered in the format: '+996 000 000 000.")


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if email is None:
            raise ValueError("users should have an email")
        user = self.model(username=username, email=self.normalize_email(
            email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Password should not be none")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=54)
    last_name = models.CharField(max_length=54)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    avatar = ContentTypeRestrictedFileField(upload_to='users/uploads/%Y/%m/%d/',
                                            content_types=['image/jpeg', 'image/png', 'image/jpg'],
                                            null=True, max_length=100, )
    city = models.CharField(max_length=12, choices=REGION_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, validators=[phone_regex], null=True, blank=True)

    provider = models.CharField(max_length=16, choices=PROVIDER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }