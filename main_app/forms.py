# forms.py
from django import forms
from .models import Character, Campaign

class CampaignCharacterForm(forms.Form):
    character = forms.ModelChoiceField(queryset=Character.objects.all(), empty_label=None)
    campaign = forms.ModelChoiceField(queryset=Campaign.objects.all(), empty_label=None)
