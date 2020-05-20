# Generated by Django 3.0.6 on 2020-05-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200515_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='feature_image_1',
            field=models.ImageField(blank=True, default='/photos/default/default.jpg', upload_to='photos/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='feature_image_2',
            field=models.ImageField(blank=True, default='/photos/default/default.jpg', upload_to='photos/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='feature_image_3',
            field=models.ImageField(blank=True, default='/photos/default/default.jpg', upload_to='photos/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='feature_image_4',
            field=models.ImageField(blank=True, default='/photos/default/default.jpg', upload_to='photos/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='feature_image_5',
            field=models.ImageField(blank=True, default='/photos/default/default.jpg', upload_to='photos/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='feature_image_6',
            field=models.ImageField(blank=True, default='/photos/default/default.jpg', upload_to='photos/property/%Y/%m/%d/'),
        ),
    ]
