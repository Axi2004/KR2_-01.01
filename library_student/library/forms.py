from django import forms
from .models import IssueRecord

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssueRecord
        fields = ['book', 'student']
        widgets = {
            'book': forms.Select(attrs={'class': 'uk-select'}),
            'student': forms.Select(attrs={'class': 'uk-select'}),
        }