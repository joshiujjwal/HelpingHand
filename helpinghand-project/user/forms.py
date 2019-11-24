from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Profile, Subject, User

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user


class InstructorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_instructor = True
        if commit:
            user.save()
        return user


class RecruiterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recruiter = True
        if commit:
            user.save()
        return user