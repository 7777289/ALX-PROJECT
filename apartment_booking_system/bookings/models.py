from django.db import models
from users.models import User
from apartments.models import Apartment

class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='bookings')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.apartment.title} by {self.tenant.username}"