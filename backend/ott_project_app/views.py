from django.shortcuts import render

from rest_framework import generics

from .models import ott_project_app
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = ott_project_app.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = ott_project_app.objects.all()
    serializer_class = PostSerializer