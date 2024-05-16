from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingsList.as_view(), name='home'),
    path('', views.CreateBooking, name='create_booking'),
]