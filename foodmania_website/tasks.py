from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rms.settings import EMAIL_HOST_USER


@shared_task()
def send_welcome_email(user_email, username):
    context = {'username': username}
    email_html = render_to_string('email/welcome_email.html', context)

    email = EmailMessage(
        subject='Welcome to Foodmania - Your Ultimate Food Destination!',
        body=email_html,
        from_email=EMAIL_HOST_USER,
        to=[user_email],
        headers={'Reply-To': EMAIL_HOST_USER}
    )
    email.send(fail_silently=True)
