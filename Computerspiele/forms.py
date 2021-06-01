from django import forms
from .models import Computerspiel


class ComputerspielForm(forms.ModelForm):

    class Meta:
        model = Computerspiel
        fields = ['name', 'beschreibung', 'developer_studio', 'genre', 'fsk', 'date_released']
        widgets = {
            'genre': forms.Select(choices=Computerspiel.GENRE),
            'ersteller': forms.HiddenInput(),
        }
