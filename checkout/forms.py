from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(1, 1) for 1 in range(1, 12)]
    YEAR_CHOICES = [(1, 1) for 1 in range(2017, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CW)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = {'full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county'}
