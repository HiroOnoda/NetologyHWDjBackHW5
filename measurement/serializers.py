from rest_framework import serializers

from measurement.models import Sensors, Measurements


# TODO: опишите необходимые сериализаторы

# class DemoSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     desc = serializers.CharField()
#
# class DemoModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensors
#         fields = ['name', 'desc']

class SensorsSerializer(serializers.ModelSerializer):
    # sensor_measurement = serializers.RelatedField(many=True,read_only=True)

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'desc']

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['sensor_id', 'temperature', 'created_at']

class SingleSensorSerializer(serializers.ModelSerializer):
    sensor_measurement = serializers.RelatedField(many=True,read_only=True)

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'desc', 'sensor_measurement']

