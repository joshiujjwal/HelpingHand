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
    user_profile = UserProfile.objects.get(user_id=request.user.id)
    enrolled_course = user_profile.enrolled_courses.all().values_list('name', flat=True)
    available_courses = list(Course.objects.exclude(name__in=enrolled_course).values_list('name', flat=True))
    #print("enrolled_course -------- ",enrolled_course)
    #print("available_courses ------- ", available_courses)
    formset = []
    for course in available_courses:
        formset.append(EnrollForm(initial={"name":course},prefix=course))
    if request.method == 'POST':
        form = EnrollForm(request.POST, prefix=list(request.POST)[1].split("-")[0])
        if form.is_valid():
            name = form.cleaned_data["name"]
            request_enroll = Course.objects.get(name=name)
            user_profile.enrolled_courses.add(request_enroll)
            return HttpResponseRedirect('/course/{}'.format(request_enroll.pk))
    return render(request, "course/dashboard.html", {"formset":formset})

@login_required
@student_required
def course(request,pk):
    course_name = Course.objects.get(id=pk)
    return render(request, "course/course.html", {"pk": pk, "course": course_name})