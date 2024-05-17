from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import generic
from django.views.generic import UpdateView, DeleteView
from .models import Bookings
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

class EditBooking(UpdateView):
    model = Bookings
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = reverse_lazy('bookings_list')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

class DeleteBooking(DeleteView):
    model = Bookings
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('bookings_list')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)





    