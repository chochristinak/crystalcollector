# Generated by Django 5.0.3 on 2024-04-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_crystal_zodiac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crystal',
            name='zodiac',
            field=models.CharField(max_length=100),
        ),
    ]
