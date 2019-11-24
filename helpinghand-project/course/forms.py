from django.forms import ModelForm
from .models import Course
from django.db import transaction
from user.models import UserProfile

class EnrollForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name',]
