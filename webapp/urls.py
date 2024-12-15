from django.urls import path
from .views import home

app_name = "webapp"

urlpatterns = [
    path('home/', home, name="home"),
]