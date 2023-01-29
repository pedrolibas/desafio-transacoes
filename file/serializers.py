from rest_framework import serializers
from .models import File
from utils.transform import convert_file
import os
from companies.serializers import CompanySerializer
from transactions.serializers import TransactionSerializer

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        file = File.objects.create(**validated_data)
        converted_file = convert_file()
        print(converted_file)
        
        for information in converted_file:
            company_dict = dict(store_owner = information.pop("store_owner"), store_name = information.pop("store_name"))
            serializer_company = CompanySerializer(data=company_dict)
            serializer_company.is_valid(raise_exception=True)
            company = serializer_company.save()[0].id

            information["company"] = company
            serializers_transaction = TransactionSerializer(data=information)
            serializers_transaction.is_valid(raise_exception=True)
            serializers_transaction.save()

        if os.path.isfile('data_file/CNAB.txt'):
            os.remove('data_file/CNAB.txt')

        return file
