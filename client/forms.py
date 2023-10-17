from django import forms
from client.models import Pending

class ComplaintForm(forms.ModelForm):
    class Meta:
        model= Pending
        fields= '__all__'

