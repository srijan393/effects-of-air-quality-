from django.shortcuts import render
from .models import RoomEffect

def home(request):
    rooms = RoomEffect.objects.all()
    return render(request, "heart_rate/home.html", {"rooms": rooms})
