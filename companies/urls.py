from django.urls import path
from .views import CompanyView, CompanyDetailView

urlpatterns = [
    path("companies/", CompanyView.as_view()),
    path("companies/<int:pk>/", CompanyDetailView.as_view())
]