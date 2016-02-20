from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
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
            message = "%s\n%s\nGuests: %s (adults), %s (children)\n%s" % (
                rsvp.name, rsvp.email, rsvp.adult_guests, rsvp.child_guests, rsvp.message
            )
            send_mail(
                subject='RSVP',
                message=message,
                from_email='www-data@ngozi-adonis.com',
                recipient_list=['adonis.ngozi@gmail.com']
            )
            response = {
                'success': True,
                'data': render_to_string('ngozi/contact.html', context={}, request=request)
            }
            return JsonResponse(response)
    else:
        form = RsvpForm()
    context = {'rsvp_form': form}
    response = {
        'success': False,
        'data': render_to_string('ngozi/modal.html', context=context, request=request)
    }
    return JsonResponse(response)
