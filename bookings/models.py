from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Submitted"), (1, "Accepted"))

# Create your models here.


class Bookings(models.Model):
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    guests_number = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    additional_reqs = models.CharField(max_length=200, blank=True, default='')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_query"
    )
    submitted_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-submitted_on"]

    def __str__(self):
        return f"{self.date} at {self.time} | {self.author}"