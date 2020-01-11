from django.contrib.auth.models import User
from django import forms
from .models import Project_Post,Reviews

class ReveiwForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude=[
            'posted_by',
            'posted_on',
            'project_id',
        ]

class Post_projectform(forms.ModelForm):
    class Meta:
        model = Project_Post
        exclude=[
            'posted_by',
            'updated_on',
        ]