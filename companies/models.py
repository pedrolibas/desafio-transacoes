from django.db import models

class Company(models.Model):
    store_owner = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
