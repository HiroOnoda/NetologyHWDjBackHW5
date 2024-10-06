# Generated by Django 5.1.1 on 2024-10-02 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('desc', models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensors')),
            ],
        ),
    ]