import datetime

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=254, blank=False, null=False)
    owner = models.CharField(max_length=254, blank=False, null=False)
    # owner should be foreign key to user model but this is out of scope, I ignored user model.


class Room(models.Model):
    listing = models.ForeignKey(Listing, related_name='rooms', on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(default=2)
    fee = models.FloatField(validators=[MinValueValidator(0.0)])

    @property
    def is_free(self, for_date=datetime.datetime.now().date()):
        return Calendar.objects.filter(room=self, listing=self.listing, date=for_date).exists()


class Reservation(models.Model):
    room = models.ForeignKey(Room, related_name='reservations', on_delete=models.CASCADE)
    reservatore = models.CharField(max_length=254, blank=False, null=False)
    reserved_from_date = models.DateTimeField()
    reserve_duration = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    reservation_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    is_checked_out = models.BooleanField(default=False)

    class Meta:
        unique_together = ('room', 'reserved_from_date')


class Calendar(models.Model):
    listing = models.ForeignKey(Listing, related_name='calendar', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='calendar', on_delete=models.CASCADE)
    date = models.DateField()
    reservation = models.ForeignKey(Reservation, related_name='calendar', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('listing', 'room', 'date')
