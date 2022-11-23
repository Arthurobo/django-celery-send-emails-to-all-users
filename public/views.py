from django.shortcuts import render
from django.contrib.auth.models import User
from .tasks import send_emails_to_users


def home_view(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    send_emails_to_users.delay()
    return render(request, 'public/home.html', context)