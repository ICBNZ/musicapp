from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Instrument, Student, Tutor, Booking


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    profile_pic = forms.ImageField(required=True)
    instrument_required = forms.BooleanField(required=True)
    instrument = forms.ModelChoiceField(queryset=Instrument.objects.all(),required=True)
    about = forms.CharField(max_length=500, required=True, help_text='About yourself.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'profile_pic',
            'instrument_required',
            'instrument',
            'about',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )
        widgets = {
            'about': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def save(self):
        user = super().save()
        return user

class TutorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    profile_pic = forms.ImageField(required=True)
    instrument_available = forms.BooleanField(required=True)
    instrument = forms.ModelChoiceField(queryset=Instrument.objects.all(),required=True)
    experience = forms.CharField(max_length=500, required=True, help_text='Your musical experience.')
    hourly_rate = forms.DecimalField(decimal_places=2)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'profile_pic',
            'instrument_available',
            'instrument',
            'experience',
            'first_name',
            'hourly_rate',
            'last_name',
            'email',
            'password1',
            'password2',
            )
        widgets = {
            'experience': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def save(self):
        user = super().save()
        return user

class BookingForm(forms.Form):
    availability = forms.BooleanField(label='Book this lesson.')
