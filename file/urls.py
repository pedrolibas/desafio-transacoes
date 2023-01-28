from django.urls import path
from .views import TransactionsView

urlpatterns = [
    path("teste/", TransactionsView.as_view())
]