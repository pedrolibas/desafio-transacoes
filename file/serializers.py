from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        file = validated_data.get("file")
        teste = File.objects.create(**validated_data)
        teste2 = open("data/CNAB.txt", "r")
        teste3 = teste2.readlines()
        print(teste3)