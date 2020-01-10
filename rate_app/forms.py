from django.contrib.auth.models import User
from django import forms
from .models import Rates,Reviews

class ReveiwForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude=[
            'posted_by',
            'posted_on',
            'project_id',
        ]

class 