# Generated by Django 3.0.6 on 2020-05-06 14:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('property_type', models.CharField(max_length=500)),
                ('reference', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('room', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('garage_area', models.DecimalField(decimal_places=1, max_digits=2)),
                ('home_area', models.DecimalField(decimal_places=1, max_digits=2)),
                ('lot_area', models.DecimalField(decimal_places=1, max_digits=2)),
                ('parking_lot', models.IntegerField()),
                ('contract', models.CharField(choices=[('RENT', 'RENT'), ('SALE', 'SALE')], default='SALE', max_length=10)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('main_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('feature_image_1', models.ImageField(blank=True, upload_to='photos/property/%Y/%m/%d/')),
                ('feature_image_2', models.ImageField(blank=True, upload_to='photos/property/%Y/%m/%d/')),
                ('feature_image_3', models.ImageField(blank=True, upload_to='photos/property/%Y/%m/%d/')),
                ('feature_image_4', models.ImageField(blank=True, upload_to='photos/property/%Y/%m/%d/')),
                ('feature_image_5', models.ImageField(blank=True, upload_to='photos/property/%Y/%m/%d/')),
                ('feature_image_6', models.ImageField(blank=True, upload_to='photos/property/%Y/%m/%d/')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agents.Agent')),
            ],
        ),
    ]
