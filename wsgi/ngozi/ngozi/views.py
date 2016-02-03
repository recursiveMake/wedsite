from django.shortcuts import render


def index(request):
    context = {
        'title': 'Ngozi and Adonis',
        'email': 'adonis@gmail.com'
    }
    return render(request, 'ngozi/index.html', context)
