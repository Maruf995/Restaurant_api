from django.contrib import admin
from reservations.models import Table, Reservation

# Register your models here.
admin.site.register(Table)
admin.site.register(Reservation)
