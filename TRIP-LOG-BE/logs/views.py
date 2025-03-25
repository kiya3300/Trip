# logs/views.py
from rest_framework import generics
from trips.models import Log
from .serializers import LogSerializer

class LogListView(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
