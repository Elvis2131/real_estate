# Generated by Django 2.2.11 on 2020-05-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Accra', 'Accra'), ('Kumasi', 'Kumasi'), ('Takoradi', 'Takoradi')], max_length=50),
        ),
    ]
