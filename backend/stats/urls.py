from django.urls import path
from .views import severity_chart

urlpatterns = [
    path("severity-chart/", severity_chart, name="severity-chart"),
]
