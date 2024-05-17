from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingsList.as_view(), name='home'),
    path('create-booking', views.CreateBooking, name='create_booking'),
    path('edit/<int:pk>/', views.EditBooking.as_view(), name='edit_booking'),
    path('delete/<int:pk>/', views.DeleteBooking.as_view(), name='delete_booking'),
]