"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from measurement.views import get_all_sensors, get_one_sensor, update_sensor, create_sensor, add_measurement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
    path('getallsensors/', get_all_sensors.as_view()),
    path('getonesensor/<pk>/', get_one_sensor.as_view()),
    path('updatesensor/<pk>/', update_sensor.as_view()),
    path('createsensor/', create_sensor.as_view()),
    path('addmeasurement/', add_measurement.as_view())
]
