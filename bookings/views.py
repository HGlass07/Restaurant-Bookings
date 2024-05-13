from django.shortcuts import render
from django.views import generic
from .models import Bookings

# Create your views here.
class BookingsList(generic.ListView):
    model = Bookings
    template_name = "bookings_list.html"

    def get_queryset(self):
        return Bookings.objects.filter(author=self.request.user)