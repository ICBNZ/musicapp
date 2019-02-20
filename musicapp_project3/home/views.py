# View.py
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tutor, Instrument, Student   # import all models
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test

# functions to get objects, classname.objects - send to url, args
#### Home
#@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'home.html')

#### Tutors
def tutors(request):
    tutors = Tutor.objects
    return render(request, 'home/tutors.html', {'tutors': tutors})

#### Students
def students(request):
    students = Student.objects
    return render(request, 'home/tutors.html', {'students': students})

#### Instruments
def instruments(request):
    instruments = Instrument.objects
    return render(request, 'home/tutors.html', {'instruments': instruments})
