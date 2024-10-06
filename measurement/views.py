# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, GenericAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensors, Measurements
from measurement.serializers import SensorsSerializer, SingleSensorSerializer, MeasurementsSerializer


# Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class get_all_sensors(APIView):
    def get(self,request):
        sensors = Sensors.objects.all()
        ser = SensorsSerializer(sensors,many=True)
        return Response(ser.data)

# Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.
class get_one_sensor(RetrieveAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SingleSensorSerializer

# Изменить датчик. Указываются название и описание.
class update_sensor(UpdateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "update successful"})

        else:
            return Response({"message": "update failed"})

# Создать датчик. Указываются название и описание датчика.
class create_sensor(CreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Добавить измерение. Указываются ID датчика и температура.
class add_measurement(CreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)