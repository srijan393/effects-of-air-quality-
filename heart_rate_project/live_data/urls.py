from django.urls import path
from .api_views import get_sensor_data, receive_sensor_data

urlpatterns = [
    path('get-data/', get_sensor_data, name='get_sensor_data'),
    path('post-data/', receive_sensor_data, name='receive_sensor_data'),
]
