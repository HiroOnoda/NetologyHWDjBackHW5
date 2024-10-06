from django.db import models

class Sensors(models.Model):

    name = models.CharField()
    desc = models.CharField(null=True, blank=True)

class Measurements(models.Model):

    sensor_id = models.ForeignKey(Sensors, on_delete = models.CASCADE,related_name='sensor_measurement')
    temperature = models.DecimalField(max_digits=4, decimal_places = 1)
    created_at = models.DateTimeField(auto_now_add = True)
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

