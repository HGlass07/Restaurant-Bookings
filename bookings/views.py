from django.shortcuts import render
from django.views import generic
from .models import Bookings

# Create your views here.
class BookingsList(generic.ListView):
    queryset = Bookings.objects.all()
    template_name = "bookings_page.html"