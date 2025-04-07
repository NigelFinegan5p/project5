from django.shortcuts import render, redirect
from .models import Voucher, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def voucher_list(request):
    # Fetch all vouchers
    vouchers = Voucher.objects.all()
    return render(request, 'book/voucher_list.html', {'vouchers': vouchers})


def book_voucher(request, voucher_id):
    # Get the voucher based on the provided voucher_id
    voucher = Voucher.objects.get(id=voucher_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking and associate it with the voucher
            booking = form.save(commit=False)
            booking.voucher = voucher  # Associate booking with the voucher
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(initial={'voucher': voucher})

    return render(request, 'hello_world/book_voucher.html', {'form': form, 'voucher': voucher})


def booking_confirmation(request, booking_id):
    # Get the booking details for confirmation
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'hello_world/booking_confirmation.html', {'booking': booking})


