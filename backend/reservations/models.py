from django.db import models

# Create your models here.
class Table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.location})'
    
class Reservation(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.customer_name} - {self.table.name} в {self.reservation_time}'