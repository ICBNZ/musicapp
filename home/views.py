# View.py
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tutor, Instrument, Student, Hour, Availablity, Booking   # import all models
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

#### sign up form
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

#### Logged In User Profile
@login_required(login_url="/accounts/login/")
def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'home/profile.html', {'user': user})


######## Class views
from django.views import generic
from django.views.generic import DetailView, TemplateView
#from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(generic.TemplateView):
    template_name = 'about.html';

class TutorView(generic.DetailView):
    model = Tutor;

def schedule(request):
    all_instruments = Instrument.objects.all()
    tutors = Tutor.objects.all()
    all_hours = Hour.objects.all()
    return render(request, 'schedule.html', {'all_instruments': all_instruments, \
        'tutors': tutors, 'all_hours': all_hours})



def detail(request, instrument_type):
    all_instruments = Instrument.objects.all()
    all_tutors = Tutor.objects.all()
    all_availablitys = Availablity.objects.all()
    return render(request, 'instrument_timetable.html', \
        {'all_instruments': all_instruments, 'all_availablitys': all_availablitys, \
        'instrument_type': instrument_type, 'all_tutors': all_tutors,})


'''
class StudentSearchView(generic.TemplateView):
    template_name = 'profile.html'
    model = Student;
@login_required(login_url="/accounts/login/")
def tutor(request, id):
    try:
        user = User.objects.get(id=id)
    except Tutor.DoesNotExist:
        raise Http404('Tutor not found')
    return render(request, 'profile.html', {'tutor': tutor})



'''
