from django.contrib.auth.models import User
from django.core.mail import send_mail

from celery import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task
def send_emails_to_users():
    users = User.objects.all()
    users_emails = []
    for user in users:
        users_emails.append(user.email)

    sending_mail = send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        [users_emails],
        fail_silently=False,
    )
    print("Voila, Email Sent to " + str(len(users)) + " users")
    return sending_mail