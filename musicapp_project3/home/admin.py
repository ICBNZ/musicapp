from django.contrib import admin
from .models import Tutor, Student, Instrument, Hour, Availablity, Booking # import models

# register models
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Instrument)

admin.site.register(Hour)
admin.site.register(Availablity)
admin.site.register(Booking)
