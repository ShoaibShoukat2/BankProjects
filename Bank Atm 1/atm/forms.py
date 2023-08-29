from django import forms
from .models import ATM

class ATMForm(forms.ModelForm):
    class Meta:
        model = ATM
        fields = ['atm_location']
