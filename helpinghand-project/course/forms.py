from django.forms import ModelForm, IntegerField
from .models import Course
from django.db import transaction
from user.models import UserProfile
from django import forms


class EnrollForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnrollForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

    class Meta:
        model = Course
        fields = ['name',]
    course_id = forms.IntegerField(widget = forms.HiddenInput(), required = False)
