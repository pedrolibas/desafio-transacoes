# Generated by Django 4.1.5 on 2023-01-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='hour',
            field=models.CharField(max_length=255),
        ),
    ]