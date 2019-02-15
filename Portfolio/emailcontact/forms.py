from django import forms
from .models import EmailContact


class EmailContactForm(forms.ModelForm):

    class Meta:
        model = EmailContact
        fields = '__all__'
