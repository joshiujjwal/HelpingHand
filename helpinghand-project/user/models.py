from django.contrib.auth.models import AbstractUser
from django.db import models
from course.models import *


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Course, related_name='interested_students')


