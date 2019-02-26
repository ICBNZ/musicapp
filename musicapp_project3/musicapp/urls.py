# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import home.views
from django.conf import settings
from django.conf.urls.static import static


# path: url, views file.profile function
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('home/', include('home.urls'))
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student', home.views.StudentSignup),
    path('accounts/signup/tutor', home.views.TutorSignup)
]
