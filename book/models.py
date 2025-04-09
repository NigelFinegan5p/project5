from django.db import models


class Voucher(models.Model):
    """
    A simple model with vouchers available for booking.

    Methods:
        __str__(): Returns the name of the voucher when the object is represented as a string.  # noqa: E501
    """

    VOUCHER_CHOICES = [
        ('voucher_1', 'Voucher 1'),
        ('voucher_2', 'Voucher 2'),
        ('voucher_3', 'Voucher 3'),
    ]

    name = models.CharField(max_length=20, choices=VOUCHER_CHOICES, unique=True)  # noqa: E501
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    A simple booking model representing 3 options ( vouchers 1 to 3).
    Methods:
        __str__(): Returns a string describing the booking, including the customer's name and voucher.  # noqa: E501
    """

    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} booked {self.voucher.name}"
