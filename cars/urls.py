from django.urls import path
from .views import CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='car-detail'),
]


# GET /api/cars/: List all cars.
# POST /api/cars/: Create a new car.
# GET /api/cars/<int:pk>/: Retrieve a specific car by ID.
# PUT /api/cars/<int:pk>/: Update a specific car by ID.
# DELETE /api/cars/<int:pk>/: Delete a specific car by ID.