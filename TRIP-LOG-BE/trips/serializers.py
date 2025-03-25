from rest_framework import serializers
from .models import DrivringTrip, OffDuty, Log

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivringTrip
        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffDuty
        fields = "__all__"

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"
