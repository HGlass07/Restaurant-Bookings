from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .models import Bookings
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class BookingsList(generic.ListView):
    model = Bookings
    template_name = "bookings_list.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Bookings.objects.filter(author=self.request.user)
        else:
            return Bookings.objects.none()

def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            bookings_count = Bookings.objects.filter(author=request.user).count()
            if bookings_count >= 2:
                messages.error(request, "You cannot have more than 2 bookings at a time.")
            else:
                booking = form.save(commit=False)
                booking.author = request.user
                booking_conflict = Bookings.objects.filter(date=booking.date, time=booking.time)
                if booking_conflict.exists():
                    messages.error(request, "This booking has been taken, please select another.")
                else:
                    booking.save()
                    messages.success(request, "Booking successful!")
                    return redirect('home') 
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})


    