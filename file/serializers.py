from rest_framework import serializers
from .models import File
from utils.transform import convert_file
import os

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        file = File.objects.create(**validated_data)
        converted_file = convert_file()
        print(converted_file)

        if os.path.isfile('data_file/CNAB.txt'):
            os.remove('data_file/CNAB.txt')

        return file
