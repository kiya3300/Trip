from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from datetime import timedelta

# class Trip(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     current_location = models.CharField(max_length=255)
#     pickup_location = models.CharField(max_length=255)
#     dropoff_location = models.CharField(max_length=255)
#     current_cycle_hours = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         # Create a new trip
#         super().save(*args, **kwargs)

#         # Create associated Route and Log after the trip is saved
#         if not self.routes.exists():
#             Route.objects.create(
#                 trip=self,
#                 route_details="Route generated for the trip",  # Placeholder for actual route details
#                 route_map_data={"map_data": "Sample map data"}  # Placeholder for actual map data
#             )

#         if not self.logs.exists():
#             Log.objects.create(
#                 trip=self,
#                 log_data={"log_details": "Initial log data"}  # Placeholder for initial log data
#             )

# class Route(models.Model):
#     trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="routes")
#     route_details = models.TextField()
#     route_map_data = models.JSONField()
#     created_at = models.DateTimeField(auto_now_add=True)


# def save(self, *args, **kwargs):
#     # Create a new trip
#     super().save(*args, **kwargs)

#     # Create associated Route and Log after the trip is saved
#     if not self.routes.exists():
#         Route.objects.create(
#             trip=self,
#             route_details="Route generated for the trip",  # Placeholder for actual route details
#             route_map_data={"map_data": "Sample map data"}  # Placeholder for actual map data
#         )

#     if not self.logs.exists():
#         Log.objects.create(
#             trip=self,
#             log_data={"log_details": "Initial log data"}  # Placeholder for initial log data
#         )


class Log(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Set ended_at to 24 hours after started_at if not already set
        if not self.ended_at:
            self.ended_at = self.started_at + timedelta(hours=24)
        super().save(*args, **kwargs)

    def is_active(self):
        # Check if the log is still active (not ended and within time)
        return self.ended_at and self.ended_at > now()


class DrivringTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    remark = models.TextField()
    log_data = models.ForeignKey(
        Log, on_delete=models.CASCADE, related_name="driving_logs"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OffDuty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_data = models.ForeignKey(
        Log, on_delete=models.CASCADE, related_name="offduty_logs"
    )

    remark = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ensure ended_at is set to 24 hours after started_at if not already set
        if not self.ended_at:
            self.ended_at = self.started_at + timedelta(hours=24)
        super().save(*args, **kwargs)


class SleepBerth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_data = models.ForeignKey(
        Log, on_delete=models.CASCADE, related_name="sleeping_logs"
    )

    remark = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ensure ended_at is set to 24 hours after started_at if not already set
        if not self.ended_at:
            self.ended_at = self.started_at + timedelta(hours=24)
        super().save(*args, **kwargs)


class OnDuty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_data = models.ForeignKey(
        Log, on_delete=models.CASCADE, related_name="onduty_logs"
    )
    remark = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ensure ended_at is set to 24 hours after started_at if not already set
        if not self.ended_at:
            self.ended_at = self.started_at + timedelta(hours=24)
        super().save(*args, **kwargs)
