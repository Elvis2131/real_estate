# Generated by Django 3.0.6 on 2020-05-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('short_note', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(blank=True, upload_to='photos/agents/%Y/%m/%d/')),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedIn', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_mvp', models.BooleanField(default=False)),
            ],
        ),
    ]