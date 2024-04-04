# Generated by Django 5.0.3 on 2024-04-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_reading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='crystal',
            name='mohs',
        ),
        migrations.RemoveField(
            model_name='crystal',
            name='shakra',
        ),
        migrations.AddField(
            model_name='crystal',
            name='collections',
            field=models.ManyToManyField(to='main_app.collection'),
        ),
    ]
