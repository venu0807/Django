from django import forms
from officer.models import Team1,Team2

class AddofficerForm(forms.ModelForm):
    class Meta:
        model = Team1
        fields = '__all__'

class AddofficerForm2(forms.ModelForm):
    class Meta:
        model = Team2
        fields = '__all__'

