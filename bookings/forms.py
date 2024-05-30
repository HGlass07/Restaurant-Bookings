from django import forms
from .models import Bookings
from datetime import datetime, timedelta


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['date', 'time', 'guests_number', 'additional_reqs']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date',
                       'min': (datetime.now() +
                               timedelta(days=7)).strftime('%Y-%m-%d'),
                       'max': (datetime.now() +
                               timedelta(days=365)).strftime('%Y-%m-%d')}),
            'time': forms.TimeInput(
                attrs={'type': 'time', 'min': '12:00', 'max': '21:00'}),
            'guests_number': forms.NumberInput
            (attrs={'min': '1', 'max': '10'}),
            'additional_reqs': forms.Textarea(attrs={
                'rows': 4, 
                'cols': 40,
                'class': 'text-area',
                }),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.now().date():
            raise forms.ValidationError("You cannot book a date in the past.")
        if date > datetime.now().date() + timedelta(days=365):
            raise forms.ValidationError
            ("You cannot book more than a year in advance.")
        return date

    def clean_time(self):
        time = self.cleaned_data['time']
        if (time < datetime.strptime('12:00', '%H:%M').time() or
           time > datetime.strptime('21:00', '%H:%M').time()):
            raise forms.ValidationError
            ("Your booking must be between 12:00 and 19:00")
        return time
