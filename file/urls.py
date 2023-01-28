from django.urls import path
from .views import FileView

urlpatterns = [
    path("teste/", FileView.as_view())
]