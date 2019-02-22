from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views

# path: url, views file.profile function
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('tutors/', views.tutors, name='tutors'),
    path('students/', views.students, name = 'students'),





    #path('tutors', views.tutors, name="tutors"),
    #path('students', views.tutors, name="students"),
    #path('tutor/<int:pk>', views.tutors, name='tour_detail'),
    #path('student/<int:id>', views.agent_account, name='agent_account'),


]
