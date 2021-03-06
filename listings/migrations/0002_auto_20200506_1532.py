# Generated by Django 3.0.6 on 2020-05-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='garage_area',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='listing',
            name='home_area',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_area',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
