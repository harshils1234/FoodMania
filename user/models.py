"""This file contains user and user address models."""

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, validate_integer
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    This model will store user details.
    """
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                  "allowed."),
    )
    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', "Female"),
        ('O', "Other")
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="user_images/",
                              default='user_images/default_profile_image.jpg')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        ordering = ['id']

    def __str__(self):
        return str(self.username)


class UserAddress(models.Model):
    """
    This model will store user address details.
    """
    TYPE = (
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Other', 'Other')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6, validators=[validate_integer])
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=TYPE)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        verbose_name_plural = 'UserAddresses'
        ordering = ['id']

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return f"{self.type} - {self.address}"
