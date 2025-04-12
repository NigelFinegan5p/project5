from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscriber, Newsletter
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save()

            # Send confirmation email
            send_mail(
                subject='Subscription Confirmation',
                message='Thank you for subscribing to our newsletter!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )

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
