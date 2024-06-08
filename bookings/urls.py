from django.urls import path
from .views import  BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='booking-detail'),
]


# GET /api/bookings/: List all bookings.
# POST /api/bookings/: Create a new booking.
# GET /api/bookings/<int:pk>/: Retrieve a specific booking by ID.
# PUT /api/bookings/<int:pk>/: Update a specific booking by ID.
# DELETE /api/bookings/<int:pk>/: Delete a specific booking by ID.