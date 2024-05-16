from django import forms
from .models import Bookings
from datetime import datetime, timedelta

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['date', 'time', 'guests_number', 'additional_reqs']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 
            'min': datetime.now() + timedelta(days=7), 
            'max': (datetime.now() + timedelta(days=365)).date()}),

            'time': forms.TimeInput(attrs={'type': 'time', 
            'min': '12:00', 'max': '21:00'}),
        }