from django.db import models

class Transaction(models.Model):
    type = models.PositiveIntegerField()
    date = models.DateField()
    value = models.FloatField()
    CPF = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.DateTimeField()
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="transactions")