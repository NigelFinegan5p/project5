from django.contrib import admin
from .models import Voucher, Booking


# Define a custom admin class for the Voucher model
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)


# Define a custom admin class for the Booking model
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'voucher', 'customer_email', 'date_booked')  # noqa: E501
    search_fields = ('customer_name', 'customer_email')
    list_filter = ('voucher', 'date_booked')
    ordering = ('-date_booked',)


# Register the models with the admin site
admin.site.register(Voucher, VoucherAdmin)
admin.site.register(Booking, BookingAdmin)




