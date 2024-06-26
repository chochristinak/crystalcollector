# Generated by Django 5.0.3 on 2024-04-03 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_crystal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='reading date')),
                ('reason', models.CharField(choices=[('H', 'Health'), ('E', 'Emotional'), ('S', 'Spiritual'), ('C', 'Career')], max_length=50)),
                ('crystal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.crystal')),
            ],
        ),
    ]
