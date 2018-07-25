from django import forms
from django.core.validators import RegexValidator

# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class ProspectCreateForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    business_email = forms.EmailField(required=False)
    company_name = forms.CharField(required=False)
    job_title = forms.CharField(required=False)
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, required=False)  # validators should be a list
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    comment = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

