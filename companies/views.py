from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer

class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer