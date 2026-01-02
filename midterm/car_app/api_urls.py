from django.urls import path
from .views import (
    cars_by_year_range,
    cars_by_fuel_type,
    high_performance_cars,
    create_car,
    delete_car,
)

urlpatterns = [
    path("cars/year/", cars_by_year_range),
    path("cars/fuel/", cars_by_fuel_type),
    path("cars/performance/", high_performance_cars),
    path("cars/create/", create_car),  
    path("cars/<int:car_id>/delete/", delete_car),
]
