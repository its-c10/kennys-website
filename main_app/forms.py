from django import forms
from django.forms.widgets import Select, TextInput
from .models import Service


class ContactForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email...",
                "class": "form-control",
                "id": "contact-page-input-email",
            }
        )
    )
    firstName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your first name...",
                "class": "form-control",
                "id": "contact-page-input-firstName",
            }
        )
    )
    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your last name...",
                "class": "form-control",
                "id": "contact-page-input-lastName",
            }
        )
    )
    phoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your phone number...",
                "class": "form-control",
                "id": "contact-page-input-phoneNumber",
            }
        )
    )
    numVehiclesDetailed = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "class": "form-range",
                "min": 0,
                "max": 10,
                "step": 1,
                "value": 1,
                "name": "car-quantity",
                "id": "car-quantity-range",
            }
        )
    )

    services = Service.objects.all()
    service_choices = ()
    service_choices_list = []
    service_count = 1
    for service in services:
        inner_tup = (service.service_type, service.service_type)
        service_choices_list.append(inner_tup)
        service_count += 1

    service_choices_list.append(("service-other", "Other"))
    service_choices = tuple(service_choices_list)

    service = forms.ChoiceField(
        choices=service_choices,
        widget=forms.Select(
            attrs={
                "class": "form-select mb-4",
                "id": "service-selection",
            }
        ),
    )

    other_service = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Specify some other service...",
                "class": "form-control",
                "id": "service-selection-other-input",
            }
        ),
    )

    nature_ack = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "value": "nature-ack-agree",
            }
        ),
    )

    photos_ack = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "value": "photos-ack-agree",
            }
        ),
    )

    photos_no = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "value": "nature-no",
            }
        ),
    )
