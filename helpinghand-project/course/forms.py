from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Course



class Course_form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','course_syllabus']

