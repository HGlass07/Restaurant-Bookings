from django.shortcuts import render, redirect
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
            booking = form.save(commit=False)
            booking.author = request.user
            booking.save()
            return redirect('bookings')  # Adjust this to your bookings list view URL name
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})


    