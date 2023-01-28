from rest_framework import generics
from .models import File
from .serializers import FileSerializer


class FileView(generics.CreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()