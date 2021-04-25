from django.forms import ModelForm
from contacts.models import * 
from listings.models import *
from realtors.models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        exclude = ['contact_date']


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['list_data']


class RealtorForm(ModelForm):
    class Meta:
        model = Realtor
        fields = '__all__'
        exclude = ['hire_date']