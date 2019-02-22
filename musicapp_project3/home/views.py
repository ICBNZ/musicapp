# View.py
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tutor, Instrument, Student   # import all models
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test

# functions to get objects, classname.objects - send to url, args
#url = reverse(view_name, args=args, kwargs=kwargs, current_app=current_app)

#### Home - passing in tutor/students
@login_required(login_url="/accounts/login/")
def home(request):
    tutors = Tutor.objects
    students = Student.objects
    return render(request, 'home.html', {'tutors': tutors},  {'students': students})



'''
# profiles
@login_required(login_url="/accounts/login/")
def profiles(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required(login_url="/accounts/login/")
def tutors(request):
    tutor = Tutor.objects
    return render(request, 'tutor.html', {'tutor': tutor})


@login_required(login_url="/accounts/login/")
def tutor(request, id):
    try:
        user = User.objects.get(id=id)
    except Tutor.DoesNotExist:
        raise Http404('Tutor not found')
    return render(request, 'profile.html', {'tutor': tutor})
'''


######## Class views
from django.views import generic
from django.views.generic import DetailView, TemplateView
#from django.contrib.auth.mixins import LoginRequiredMixin

class TutorSearchView(generic.TemplateView):
    template = 'profile.html'
    model = Tutor
    #paginate_by = 10

class StudentSearchView(generic.TemplateView):
    template_name = 'profile.html'
    model = Student
    #paginate_by = 10