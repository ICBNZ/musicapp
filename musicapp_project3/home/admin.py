from django.contrib import admin
from .models import Tutor, Student, Instrument # import models

# register models
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Instrument)
