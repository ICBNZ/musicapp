from django.contrib import admin
from .models import Tutor, Student, Instrument, Availability, Hour, Booking # import models

# register models
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Instrument)

@admin.register(Hour)
class Hour(admin.ModelAdmin):
    list_display = ['day_of_week', 'hour']


@admin.register(Availability)
class Availability(admin.ModelAdmin):
    list_display = ['tutor', 'hour', 'available']

admin.site.register(Booking)
