from django.urls import path
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

# path: url, views file.profile function
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('tutors', views.TutorListView.as_view(), name='tutors'),
    path('tutor/<pk>', views.TutorDetailView.as_view(), name='tutor_detail'),

    path('students', views.StudentListView.as_view(), name='students'),
    path('student/<pk>', views.StudentDetailView.as_view(), name='student_detail'),

    path('profile/<id>', views.profile, name='profile'),

    path('profile/edit/redirect/', views.ProfileEditRedirect, name='profile_edit_redirect'),
    path('profile/edit/student/', views.StudentUpdate.as_view(), name='student_edit'),
    path('profile/edit/tutor/', views.TutorUpdate.as_view(), name='tutor_edit'),

    path('about', views.AboutView.as_view(), name='about'),

    path('schedule/', views.schedule, name = 'schedule'),
    re_path(r'^schedule/(?P<instrument_type>[\w-]+)/$', views.detail, name = 'detail'),

	re_path(r'^booking/(?P<pk>[0-9]+)/$', views.booking_page, name = 'booking'),
    path('booking_confirmed', views.BookedView.as_view(), name='booking_confirmed'),
    path('book/<pk>', views.book, name = 'book'),
]
