from django import forms
from .models import MembershipApplication


class MembershipApplicationForm(forms.ModelForm):

    class Meta:

        model = MembershipApplication

        fields = [
            "email",
            "name",
            "postcode",
            "phone",
        ]

        widgets = {

            "email": forms.EmailInput(attrs={
                "placeholder": "Your email",
                "autocomplete": "email",
            }),

            "name": forms.TextInput(attrs={
                "placeholder": "Your answer",
                "autocomplete": "name",
            }),

            "postcode": forms.TextInput(attrs={
                "placeholder": "Your answer",
                "autocomplete": "postal-code",
            }),

            "phone": forms.TextInput(attrs={
                "placeholder": "Your answer",
                "type": "tel",
                "autocomplete": "tel",
            }),

        }

        labels = {
            "email": "Email",
            "name": "Name",
            "postcode": "Post Code Area (UB, HA, IG, SL, WD etc)",
            "phone": "Phone Number",
        }

    def clean_postcode(self):

        return self.cleaned_data["postcode"].strip().upper()