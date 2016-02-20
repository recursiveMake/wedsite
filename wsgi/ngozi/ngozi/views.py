from django.core.mail import send_mail
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from ngozi.forms import RsvpForm


def index(request):
    context = {
        'title': 'Ngozi and Adonis',
        'email': 'adonis@gmail.com'
    }
    return render(request, 'ngozi/index.html', context)


@require_POST
@csrf_protect
def rsvp(request):
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            rsvp = form.save()
            message = "%s\n%s\nGuests: %s\n%s" % (rsvp.name, rsvp.email, rsvp.guests, rsvp.message)
            send_mail(
                subject='RSVP',
                message=message,
                from_email='www-data@ngozi-adonis.com',
                recipient_list=['adonis.ngozi@gmail.com']
            )
            return TemplateResponse(request, 'ngozi/contact.html', {})
    else:
        form = RsvpForm()
    context = {'form': form}
    return TemplateResponse(request, 'ngozi/rsvp.html', context)
