# View.py
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tutor, Instrument, Student   # import all models
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test

# functions to get objects, classname.objects - send to url, args
'''edef login(request):
    return render(request, 'login.html')
'''

#### Home
@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'home.html')

#### Tutors
def tutors(request):
    tutors = Tutor.objects
    return render(request, 'tutors.html', {'tutors': tutors})

#### Students
def students(request):
    students = Student.objects
    return render(request, 'students.html', {'students': students})


######## Class views
from django.views import generic
from django.views.generic import DetailView, TemplateView
#from django.contrib.auth.mixins import LoginRequiredMixin
'''
class TutorSearchView(generic.TemplateView):
    template_name = 'tutors.html'
    model = Tutor
    #paginate_by = 10

class StudentSearchView(generic.TemplateView):
    template_name = 'students.html'
    model = Student
    #paginate_by = 10
'''
