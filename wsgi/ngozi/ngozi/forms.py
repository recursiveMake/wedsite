from django.forms import ModelForm

from ngozi.models import Rsvp


class RsvpForm(ModelForm):
    class Meta:
        model = Rsvp
        fields = ['name', 'email', 'adult_guests', 'child_guests' 'message']
