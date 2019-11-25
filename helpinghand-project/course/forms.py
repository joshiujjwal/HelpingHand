from django.forms import ModelForm
from .models import Course
from django.db import transaction
from user.models import UserProfile

class EnrollForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnrollForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

    class Meta:
        model = Course
        fields = ['name',]
