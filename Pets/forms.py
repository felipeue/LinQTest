from django import forms
from Pets.models import *


class OwnerForm(forms.ModelForm):
    nickname = forms.CharField(max_length=90)

    class Meta:
        model = Owner
        fields = ('nickname',)


class PetForm(forms.ModelForm):
    name = forms.CharField(max_length=90)

    class Meta:
        model = Pet
        fields = ('name', 'picture')