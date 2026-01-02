from django.shortcuts import render
from .models import Car
import re
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer

# Create your views here.
def index(request):
    return render(request, "car_app/index.html")

def car_list(request):
    cars = Car.objects.all()

    start = request.GET.get("start")
    end = request.GET.get("end")
    fuel = request.GET.get("fuel")
    high_perf = request.GET.get("high_perf")

    # Year filter
    if start and end:
        cars = cars.filter(
            production_year__gte=start,
            production_year__lte=end
        )

    # Fuel filter
    if fuel:
        cars = cars.filter(fuel__iexact=fuel)

    # High performance filter (reuse your logic)
    if high_perf:
        filtered = []
        for car in cars.exclude(top_speed__in=["", "N/A", "nan", "NaN", None]):
            match = re.search(r"\d+(\.\d+)?", car.top_speed)
            if match and float(match.group()) >= 150:
                filtered.append(car)
        cars = filtered

    return render(request, "car_app/car_list.html", {"cars": cars})

# Filter cars by production year range
@api_view(["GET"])
def cars_by_year_range(request):
    start = request.GET.get("start")
    end = request.GET.get("end")

    if not start or not end:
        return Response(
            {"error": "Please provide start and end year"},
            status=400
        )

    cars = Car.objects.filter(
        production_year__gte=start,
        production_year__lte=end
    )

    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

# High performance cars
@api_view(["GET"])
def high_performance_cars(request):
    cars = Car.objects.exclude(top_speed__in=["", "N/A", "nan", "NaN", None])
    high_perf = []

    for car in cars:
        match = re.search(r"\d+(\.\d+)?", car.top_speed)
        if match:
            speed = float(match.group())
            if speed >= 150:
                high_perf.append(car)

    serializer = CarSerializer(high_perf, many=True)
    return Response(serializer.data)

# Car's fuel types
@api_view(["GET"])
def cars_by_fuel_type(request):
    fuel_type = request.GET.get("type")

    if not fuel_type:
        return Response(
            {"error": "Please provide a fuel type, e.g. ?type=Gasoline"},
            status=400
        )

    cars = Car.objects.filter(fuel__iexact=fuel_type)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

# POST cars
@api_view(["POST"])
def create_car(request):
    serializer = CarSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

def create_car_page(request):
    if request.method == "POST":
        serializer = CarSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect("home")
        else:
            print(serializer.errors)

    return render(request, "car_app/create_car.html")

# Delete car
@api_view(["DELETE"])
def delete_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
        return Response(
            {"message": f"Car with id {car_id} deleted successfully"},
            status=200
        )
    except Car.DoesNotExist:
        return Response(
            {"error": "Car not found"},
            status=404
        )

def delete_car_page(request, car_id):
    if request.method == "POST":
        Car.objects.filter(id=car_id).delete()
    return redirect("home")
