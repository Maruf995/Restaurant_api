from datetime import timedelta

from rest_framework import serializers
from django.db.models import Q 

from .models import Table, Reservation


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        start_time = data['reservation_time']
        end_time = start_time + timedelta(minutes=data['duration_minutes'])
        table = data['table']

        conflicts = Reservation.objects.filter(
            table=table
        ).filter(
            Q(reservation_time__lt=end_time) & 
            Q(reservation_time__gte=start_time - timedelta(minutes=data['duration_minutes']))
        )
        if self.instance:
            conflicts = conflicts.exclude(id=self.instance.id)

        if conflicts.exists():
            raise serializers.ValidationError("Это время уже занято.")

        return data