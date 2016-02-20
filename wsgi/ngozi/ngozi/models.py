from django.db import models
from django.db.models import CharField, EmailField, DateTimeField, TextField


class GuestCount(object):

    NONE = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'

    COUNTS = (
        (NONE, 'None'),
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
    )


class Rsvp(models.Model):
    name = CharField(max_length=128)
    email = EmailField()
    adult_guests = CharField(max_length=1, choices=GuestCount.COUNTS, default=GuestCount.TWO, verbose_name='Adult Guests')
    child_guests = CharField(max_length=1, choices=GuestCount.COUNTS, default=GuestCount.NONE, verbose_name='Children')
    entered = DateTimeField(auto_now_add=True)
    message = TextField(max_length=4096, blank=True, null=True)
