from django import forms
from .models import Booking, Voucher


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['voucher', 'customer_name', 'customer_email']

    voucher = forms.ModelChoiceField(queryset=Voucher.objects.all(), empty_label="Select a Voucher")
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()


