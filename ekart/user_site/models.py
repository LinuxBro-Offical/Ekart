from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.deletion import PROTECT
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
from admin_dashboard.models import Category, Offer,SubCategory,Product


class Enduser(AbstractBaseUser, PermissionsMixin):
    mobile = PhoneNumberField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'mobile'
    objects = CustomUserManager()

    def __str__(self):
        return str(self.mobile)


class DisplayDeals(models.Model):
    deal_name = models.CharField(max_length=50)
    offer = models.ForeignKey(Offer, on_delete=PROTECT, blank=True, null=True)
    product = models.ManyToManyField(Product)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.deal_name)
