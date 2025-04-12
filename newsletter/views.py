from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscriber, Newsletter
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save()

            subject = 'Subscription Confirmation'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = subscriber.email

            # Text & HTML content
            text_content = 'Thank you for subscribing to our newsletter.'
            html_content = render_to_string('newsletter/subscription_confirmation_email.html')

            # Build and send the email
            email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            email.attach_alternative(html_content, "text/html")
            email.send()

            messages.success(request, 'Thank you for subscribing! A confirmation email has been sent.')
            return redirect('subscribe_success')
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})



def newsletter_list(request):
    newsletters = Newsletter.objects.all().order_by('-created_on')
    return render(request, 'newsletter/newsletter_list.html', {'newsletters': newsletters})  # noqa:E501


def subscribe_success(request):
    return render(request, 'newsletter/subscribe_success.html')
