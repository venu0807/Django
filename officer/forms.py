from django import forms
from officer.models import Team1

class addofficer(forms.ModelForm):
    class Meta:
        model = Team1
        fields = '__all__'