from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer

@api_view(['GET'])
def get_sensor_data(request):
    data = SensorData.objects.all().order_by('-timestamp')[:10]  # Get last 10 readings
    serializer = SensorDataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def receive_sensor_data(request):
    serializer = SensorDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
