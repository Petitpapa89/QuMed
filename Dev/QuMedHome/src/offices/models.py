from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Prospect(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    business_email = models.EmailField(max_length=120, null=True, blank=True)
    company_name = models.CharField(max_length=120, null=True, blank=True)
    job_title = models.CharField(max_length=120, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)  # validators should be a list
    city = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # creating slugs
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.company_name

    @property
    def title(self):
        return self.company_name  # obj.tiletile


def off_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def off_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save(# )


pre_save.connect(off_pre_save_receiver, sender=Prospect)

# post_save.connect(off_post_save_receiver, sender=Office)
