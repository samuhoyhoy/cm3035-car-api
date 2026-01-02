from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("car_app.urls")),        # HTML
    path("api/", include("car_app.api_urls")), # API
]
