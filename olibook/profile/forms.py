from django import forms
from profile.models import *

class ProfilePictureForm(forms.ModelForm):

    class Meta:
        model = ProfilePicture
        exclude = ['user']
