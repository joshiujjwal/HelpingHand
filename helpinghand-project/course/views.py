from django.shortcuts import render
from user.decorators import *
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Course

from .forms import Course_form

# Create your views here.
@login_required
@instructor_required
def course_upload(request):
    course = Course.objects.all()
    course_form = Course_form()
    if request.method == "POST":
        course_form = Course_form(request.POST, request.FILES)

        if course_form.is_valid():
            course_form.save()
            return redirect('home')
    return render(request, 'course_addition.html', {"course_form":course_form})


