from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views

# path: url, views file.profile function
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('tutor/<id>', views.TutorView.as_view(), name='tutor'),
    path('profile/<id>', views.profile, name='profile'),
    path('about', views.AboutView.as_view(), name='about'),


]




'''
path('tutor/<id>', views.TutorSearchView.as_view(), name='tutors'),
path('tutors', views.tutor, name='tutors'),
path('students', views.student, name='students'),
path('student/<id>', views.StudentSearchView.as_view(), name='student'),
'''
