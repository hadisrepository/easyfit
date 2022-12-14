from django import forms

from .models import Customer


class BookForCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','surname','email','phone_number']
