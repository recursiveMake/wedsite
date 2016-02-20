from django.db import models
from django.db.models import CharField, EmailField, SmallIntegerField, DateTimeField, TextField


class Rsvp(models):
    name = CharField(max_length=128)
    email = EmailField()
    guests = SmallIntegerField(default=True, verbose_name='number of guests')
    entered = DateTimeField(auto_now_add=True)
    message = TextField(max_length=4096)
