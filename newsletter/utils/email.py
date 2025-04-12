from django.core.mail import send_mail
from .models import Subscriber


def send_newsletter(newsletter):
    subscribers = Subscriber.objects.values_list('email', flat=True)
    send_mail(
        subject=newsletter.subject,
        message=newsletter.content,
        from_email='your-email@example.com',
        recipient_list=subscribers,
    )
