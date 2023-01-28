from rest_framework import serializers
from .models import File
from utils.transform import convert_file
import os
from companies.serializers import CompanySerializer

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        file = File.objects.create(**validated_data)
        converted_file = convert_file()
        
        for information in converted_file:
            company = dict(store_owner = information.pop("store_owner"), store_name = information.pop("store_name"))
            serializer = CompanySerializer(data=company)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        if os.path.isfile('data_file/CNAB.txt'):
            os.remove('data_file/CNAB.txt')

        return file
