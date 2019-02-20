from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views

# path: url, views file.profile function
urlpatterns = [
    path('', views.home, name='home'),
    path('tutors', views.tutors, name="tutors"),

]
