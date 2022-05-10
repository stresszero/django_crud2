from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("owners/", include("owners.urls")),
    path("movies/", include("movies.urls")),
]
