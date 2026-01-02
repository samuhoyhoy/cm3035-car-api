from django.core.management.base import BaseCommand
import pandas as pd
from car_app.models import Car

class Command(BaseCommand):
    help = "Import cars from CSV into the database"

    def handle(self, *args, **kwargs):
        # Update path to your CSV
        df = pd.read_csv('data/cars-cleaned.csv')

        # Drop existing entries to avoid duplicates
        Car.objects.all().delete()

        # Loop through rows and create Car objects
        for _, row in df.iterrows():
            year = row.get("Production years")
            if year is None or pd.isna(year):
                continue
            years = int(year)

            Car.objects.create(
                model=row.get("Model"),
                series=row.get("Serie"),
                company=row.get("Company"),
                body_style=row.get("Body style"),
                segment=row.get("Segment"),
                production_year=years,
                cylinders=row.get("Cylinders"),
                displacement=row.get("Displacement"),
                horsepower=row.get("Power(HP)"),
                torque_nm=row.get("Torque(Nm)"),
                fuel=row.get("Fuel"),
                top_speed=row.get("Top Speed"),
                acceleration=row.get("Acceleration 0-62 Mph (0-100 kph)"),
                drive_type=row.get("Drive Type"),
                gearbox=row.get("Gearbox"),
                unladen_weight=row.get("Unladen Weight")
            )

        self.stdout.write(self.style.SUCCESS("Cars imported successfully!"))
