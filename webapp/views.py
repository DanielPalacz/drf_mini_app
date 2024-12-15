from django.shortcuts import render
import requests

def home(request):
    response = requests.get("http://127.0.0.1:8000/posts/", timeout=5)
    data = response.json()

    return render(request, "webapp/home.html", context={"data": data})
