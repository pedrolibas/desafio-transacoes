from rest_framework import serializers
from .models import Company
from transactions.serializers import TransactionSerializer

class CompanySerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    account_balance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

    def get_account_balance(self, obj):
        total_value = 0
        transactions = TransactionSerializer(obj.transactions, many=True)
        for transation in transactions.data:
            if transation["type"]== 2 or transation["type"]== 3 or transation["type"]== 9:
                total_value -= transation["value"]
            else:
                total_value += transation["value"]

        return round(total_value, 2)

    def create(self, validated_data):
        return Company.objects.get_or_create(**validated_data)