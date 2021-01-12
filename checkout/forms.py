"""Order detail form and credit card payment form"""
from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    """For entering credit card details"""
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    credit_card_number = forms.CharField(
        label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """for entering address details of the order"""
    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )
        widgets = {
            'full_name': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'phone_number': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'country': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'postcode': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'town_or_city': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'street_address1': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'street_address2': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"}),
            'county': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'onblur': "storeFormField()"})
        }
