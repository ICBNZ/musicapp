from django.urls import path
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

# path: url, views file.profile function
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    #path('search', views.search, name='search'),

    path('tutors', views.TutorListView.as_view(), name='tutors'),
    path('tutor/<pk>', views.TutorDetailView.as_view(), name='tutor_detail'),

    path('students', views.TutorListView.as_view(), name='students'),
    path('student/<pk>', views.TutorDetailView.as_view(), name='student_detail'),

    path('profile/<id>', views.profile, name='profile'),
    path('about', views.AboutView.as_view(), name='about'),

    path('schedule/', views.schedule, name = 'schedule'),
    re_path(r'^schedule/(?P<instrument_type>[\w-]+)/$', views.detail, name = 'detail'),



]




'''
path('tutor/<id>', views.TutorSearchView.as_view(), name='tutors'),
path('tutors', views.tutor, name='tutors'),
path('students', views.student, name='students'),
path('student/<id>', views.StudentSearchView.as_view(), name='student'),
'''
