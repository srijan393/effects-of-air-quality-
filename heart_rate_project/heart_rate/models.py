from django.db import models


class RoomEffect(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    from django.db import models

    class SensorData(models.Model):
        temperature = models.FloatField()
        humidity = models.FloatField()
        air_quality = models.FloatField()
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Temp: {self.temperature}, Humidity: {self.humidity}, Air Quality: {self.air_quality}"

