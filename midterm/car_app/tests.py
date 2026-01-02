from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Car

# Create your tests here.
class CarAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create a sample car for GET tests
        self.car = Car.objects.create(
            model="Test Model",
            series="Test Series",
            company="Test Company",
            production_year=2020,
            cylinders="L4",
            displacement=2000,
            horsepower="200 HP",
            torque_nm="300 Nm",
            fuel="Gasoline",
            top_speed="150",
            acceleration="7.5 s",
            drive_type="FWD",
            gearbox="Automatic",
            unladen_weight="3200"
        )

    def test_get_cars_by_year_range(self):
        # Test GET cars filtered by year range
        response = self.client.get(
            "/api/cars/year/?start=2019&end=2021"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_car(self):
        # Test POST create a new car
        data = {
            "model": "New Test Car",
            "series": "API Series",
            "company": "API Motors",
            "production_year": 2024,
            "cylinders": "L4",
            "displacement": 1800,
            "horsepower": "180 HP",
            "torque_nm": "250 Nm",
            "fuel": "Gasoline",
            "top_speed": "140",
            "acceleration": "8.0 s",
            "drive_type": "FWD",
            "gearbox": "Manual",
            "unladen_weight": "3000"
        }

        response = self.client.post(
            "/api/cars/create/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 2)