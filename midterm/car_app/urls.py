from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("cars/", views.car_list, name="car_list"),
    path("create/", views.create_car_page, name="create_car_page"),
    path("delete/<int:car_id>/", views.delete_car_page, name="delete_car_page"),
]
