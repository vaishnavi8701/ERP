from django import forms
from marketing.models import Emp_Quot

class FileForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Emp_Quot
        fields = ('source_code',)
