# View.py
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from home.forms import StudentSignUpForm, TutorSignUpForm
from .models import Tutor, Instrument, Student, Hour, Availablity, Booking   # import all models
from django.db.models import Q # import for searching

# functions to get objects, classname.objects - send to url, args
#url = reverse(view_name, args=args, kwargs=kwargs, current_app=current_app)

#### Home - passing in tutor/students
@login_required(login_url="/accounts/login/")
def home(request):
    tutor_search = ''
    student_search = ''
    tutors = Tutor.objects.all()
    students = Student.objects.all()

    # search bar
    if 'student_search' in request.GET:
        student_search = request.GET['student_search']
        tutors = tutors.filter(Q(instrument__name__icontains=student_search))
    elif 'tutor_search' in request.GET:
        student_search = request.GET['student_search']
        students = students.filter(Q(instruments__name__icontains=student_search))

    return render(request, 'home.html', {'tutors': tutors,'students': students,'student_search': student_search})



#### sign up form
def StudentSignup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            student = Student(
                user = authenticate(username=username, password=raw_password),
                profile_pic = form.cleaned_data.get('profile_pic'),
                name = (form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')),
                about = form.cleaned_data.get('about'),
                instrument_req = form.cleaned_data.get('instrument_required'),
                instrument = form.cleaned_data.get('instrument'),
                )
            student.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = StudentSignUpForm()
    return render(request, 'registration/studentsignup.html', {'form': form})

#### tutor sign up form
def TutorSignup(request):
    if request.method == 'POST':
        form = TutorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            tutor = Tutor(
                user = authenticate(username=username, password=raw_password),
                profile_pic = form.cleaned_data.get('profile_pic'),
                name = (form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')),
                experience = form.cleaned_data.get('experience'),
                instrument_avail = form.cleaned_data.get('instrument_available'),
                instrument = form.cleaned_data.get('instrument'),
                price = form.cleaned_data.get('hourly_rate'),
                )
            tutor.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = TutorSignUpForm()
    return render(request, 'registration/tutorsignup.html', {'form': form})

#### Logged In User Profile
@login_required(login_url="/accounts/login/")
def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'home/profile.html', {'user': user})

### Booking
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


from django.views import generic
from django.views.generic import DetailView, TemplateView
#from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(generic.TemplateView):
    template_name = 'about.html';

class TutorView(generic.DetailView):
    model = Tutor;
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
