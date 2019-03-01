# View.py
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from home.forms import StudentSignUpForm, TutorSignUpForm
from .models import Tutor, Instrument, Student, Hour, Availablity, Booking   # import all models
from django.db.models import Q # import for searching
from django.shortcuts import render, get_object_or_404
# functions to get objects, classname.objects - send to url, args
#url = reverse(view_name, args=args, kwargs=kwargs, current_app=current_app)

#### Home - passing in tutor/students
@login_required(login_url="/accounts/login/")
def home(request):
    tutors = Tutor.objects
    students = Student.objects
    return render(request, 'home.html', {'tutors': tutors},  {'students': students})

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

### redirects to the right profile editor
@login_required(login_url="/accounts/login/")
def ProfileEditRedirect(request):
    if request.user.student:
        return redirect('/home/profile/edit/student/')
    if request.user.tutor:
        return redirect('tutor/')

## BOOKING
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

## PROFILES VIEW/SEARCH
## Details
@login_required(login_url="/accounts/login/")
def tutor_detail(request, pk):
    tutor = get_object_or_404(Post, pk=pk)
    return render(request, 'tutor_detail.html', {'tutor': tutor})

@login_required(login_url="/accounts/login/")
def student_detail(request, pk):
    tutor = get_object_or_404(Post, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

######## Class views
from django.views import generic
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import UpdateView
import functools
#from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = ['profile_pic', 'name', 'about', 'instrument', 'instrument_req']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(StudentUpdate, self).get_form(form_class)
        form.fields['instrument_req'].label = 'Instrument Required'
        return form

    def get_object(self):
        return get_object_or_404(Student, pk=Student(user=self.request.user))

class TutorUpdate(UpdateView):
    model = Tutor
    fields = ['profile_pic', 'name', 'experience', 'instrument', 'instrument_avail']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(TutorUpdate, self).get_form(form_class)
        form.fields['instrument_avail'].label = 'Instrument Available'
        return form

    def get_object(self):
        return get_object_or_404(Tutor, pk=Tutor(user=self.request.user))

class StudentListView(generic.ListView):
    model = Student
    def get_queryset(self):
        result = super(StudentListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(Q(name__icontains=query) |
                (Q(about__icontains=query) |
                (Q(instrument__name__icontains=query)))
            )
        return result


class TutorDetailView(generic.DetailView):
    model = Tutor

class StudentDetailView(generic.DetailView):
    model = Student

class TutorListView(generic.ListView):
    model = Tutor
    def get_queryset(self):
        result = super(TutorListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(Q(name__icontains=query) |
                (Q(experience__icontains=query) |
                (Q(instrument__name__icontains=query)))
            )
        return result
