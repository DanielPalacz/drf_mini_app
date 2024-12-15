from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by("title")
    serializer_class = PostsSerializer
