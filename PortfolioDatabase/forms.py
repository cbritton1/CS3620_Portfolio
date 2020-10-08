from django import forms
from .models import Contact, Portfolio


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['item_name', 'item_desc', 'item_image']
