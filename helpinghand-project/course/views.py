from django.shortcuts import HttpResponseRedirect,render, redirect
from  django.forms import formset_factory
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from user.decorators import student_required

from user.models import User
from .models import Course


@login_required
@student_required
def dashboard(request):
    form = EnrollForm(initial={"name": "qweer"})
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            user = User.objects.get(id=request.user.id)
            user_profile = UserProfile.objects.get(user=user)
            enrolled_courses = user_profile.enrolled_courses.filter(name=name)
            if len(enrolled_courses) == 0:
                enrolled_course = user_profile.enrolled_courses.create(name=name)
                return HttpResponseRedirect('/course/{}'.format(enrolled_course.pk))
            
    return render(request, "course/dashboard.html", {"form":form})

@login_required
@student_required
def course(request,pk):
    course_name = Course.objects.get(id=pk)
    return render(request, "course/course.html", {"pk": pk, "course": course_name})