from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    type = models.CharField(max_length=120, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name