from django.utils.timezone import now
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from trips.utils.active_log import end_active_status
from .models import DrivringTrip, OffDuty, Log, OnDuty, SleepBerth
from .serializers import TripSerializer, LogSerializer

# class TripListCreateView(generics.ListCreateAPIView):
#     queryset = DrivringTrip.objects.all()
#     serializer_class = TripSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         # Save the trip and link it to the authenticated user
#         trip = serializer.save(user=self.request.user)

#         # Create a related route for the newly created trip
#         OffDuty.objects.create(
#             trip=trip,
#             route_details="Route generated for the trip",  # Default placeholder for route details
#             route_map_data={"map_data": "Sample map data"}  # Default placeholder for route map data
#         )

#         # Create the associated log
#         Log.objects.create(
#             trip=trip,
#             log_data={"log_details": "Initial log data"}  # Default placeholder for log data
#         )

#     def create(self, request, *args, **kwargs):
#         # Handle the creation of the trip and related data
#         response = super().create(request, *args, **kwargs)
#         return Response({
#             "message": "Trip created successfully!",
#             "trip_id": response.data['id']
#         }, status=status.HTTP_201_CREATED)


# class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DrivringTrip.objects.all()
#     serializer_class = TripSerializer
#     permission_classes = [IsAuthenticated]


# class RouteListCreateView(generics.ListCreateAPIView):
#     queryset = OffDuty.objects.all()
#     serializer_class = RouteSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         # Ensure the trip is valid and related
#         trip = serializer.validated_data.get('trip')
#         if not trip:
#             raise ValueError("Trip is required")
#         serializer.save()


# class RouteDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OffDuty.objects.all()
#     serializer_class = RouteSerializer
#     permission_classes = [IsAuthenticated]


# class LogListCreateView(generics.ListCreateAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         # Ensure the trip is valid and related
#         trip = serializer.validated_data.get('trip')
#         if not trip:
#             raise ValueError("Trip is required")
#         serializer.save()


# class LogDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer
#     permission_classes = [IsAuthenticated]


class StartLog(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Ensure 'remark' is provided
        remark = request.data.get("remark")
        if not remark:
            return Response(
                {"error": "Remark is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Handle the creation of the log
        response = super().create(request, *args, **kwargs)
        OnDuty.objects.create(
            user=self.request.user,
            log_data=response.data["id"],
            remark=remark,
        )
        return Response(
            {"message": "Log started!", "log_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )


class startDriving(generics.CreateAPIView):
    queryset = DrivringTrip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Handle the creation of the trip and related data
        user = self.request.user

        response = super().create(request, *args, **kwargs)
        log = Log.objects.filter(
            user=self.request.user,
            ended_at__gt=now(),  # Ensure the log's ended_at is in the future
        ).last()

        end_active_status(user, log)

        # Step 4: Create a new Driving Trip
        request.data["log_data"] = log.id  # Associate trip with the active log
        response = super().create(request, *args, **kwargs)

        return Response(
            {"message": "Trip started!", "trip_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )


class startSleepBreth(generics.CreateAPIView):
    queryset = SleepBerth.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Handle the creation of the trip and related data
        user = self.request.user
        response = super().create(request, *args, **kwargs)
        log = Log.objects.filter(
            user=self.request.user,
            ended_at__gt=now(),  # Ensure the log's ended_at is in the future
        ).last()

        end_active_status(user, log)

        # Step 4: Create a new Driving Trip
        request.data["log_data"] = log.id  # Associate trip with the active log
        response = super().create(request, *args, **kwargs)

        return Response(
            {"message": "Trip started!", "trip_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )


class StartOffDuty(generics.CreateAPIView):
    queryset = OffDuty.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Handle the creation of the trip and related data
        user = self.request.user
        response = super().create(request, *args, **kwargs)
        log = Log.objects.filter(
            user=self.request.user,
            ended_at__gt=now(),  # Ensure the log's ended_at is in the future
        ).last()

        end_active_status(user, log)

        # Step 4: Create a new Driving Trip
        request.data["log_data"] = log.id  # Associate trip with the active log
        response = super().create(request, *args, **kwargs)

        return Response(
            {"message": "Trip started!", "trip_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )


class StartOnDuty(generics.CreateAPIView):
    queryset = OnDuty.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Handle the creation of the trip and related data
        user = self.request.user
        response = super().create(request, *args, **kwargs)
        log = Log.objects.filter(
            user=self.request.user,
            ended_at__gt=now(),  # Ensure the log's ended_at is in the future
        ).last()

        end_active_status(user, log)

        # Step 4: Create a new Driving Trip
        request.data["log_data"] = log.id  # Associate trip with the active log
        response = super().create(request, *args, **kwargs)

        return Response(
            {"message": "Trip started!", "trip_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )


class LogOffDuty(generics.CreateAPIView):
    queryset = OffDuty.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Ensure 'remark' is provided
        user = self.request.user
        log = Log.objects.filter(
            user=user,
            ended_at__gt=now(),  # Ensure the log's ended_at is in the future
        ).last()
        # Handle the creation of the log
        end_active_status(user, log)
        return Response(
            {
                "message": "Log Off!",
            },
            status=status.HTTP_201_CREATED,
        )


class LogView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the trip is valid and related
        trip = serializer.validated_data.get("trip")
        if not trip:
            raise ValueError("Trip is required")
        serializer.save()

    def create(self, request, *args, **kwargs):
        # Handle the creation of the trip and related data
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Trip created successfully!", "trip_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )
