# View.py
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from home.forms import SignUpForm
from .models import Tutor, Instrument, Student   # import all models
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
        tutors = tutors.filter(Q(instruments__icontains=student_search))
    elif 'tutor_search' in request.GET:
            student_search = request.GET['student_search']
            students = students.filter(Q(instruments__icontains=student_search))

    return render(request, 'home.html', {'tutors': tutors,'students': students,'student_search': student_search})



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
