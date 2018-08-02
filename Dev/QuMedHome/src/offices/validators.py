from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
        )


def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("We do not accept edu emails")


JOBTTILE = ['Dev', 'Sales', 'CSR']


def validate_job_title(value):
    title = value.capitalize()
    if value not in JOBTTILE and title not in JOBTTILE:
        raise ValidationError(
                "{} is not a valid job title".format(value)
        )
