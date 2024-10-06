# Generated by Django 5.1.1 on 2024-10-05 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_measurement', to='measurement.sensors'),
        ),
    ]