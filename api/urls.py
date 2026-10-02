"""
SVCloud API URL configuration.

Stage 1: Health check endpoint only.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.HealthCheckView.as_view(), name="health-check"),
]
