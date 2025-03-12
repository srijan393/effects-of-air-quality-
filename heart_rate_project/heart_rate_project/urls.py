from django.contrib import admin
from django.urls import path, include
from live_data.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("live_data.urls")),
    path("", home),
]
