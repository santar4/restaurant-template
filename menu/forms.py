from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'guests', 'date', 'time', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ваше ім\'я'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '+380 XX XXX XX XX'
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control', 'min': 1, 'max': 20
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control', 'type': 'time'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'placeholder': 'Особливі прохання (опційно)'
            }),
        }
