from django import forms
from .models import Profile, Room


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['icon', 'bio']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']
