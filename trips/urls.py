from django.urls import path
from .views import (
    StartLog,
    startDriving,
    startSleepBreth,
    StartOffDuty,
    StartOnDuty,
    LogOffDuty,
    LogView,
)

urlpatterns = [
    path("logs/start/", StartLog.as_view(), name="start-log"),
    path("trip/start-driving/", startDriving.as_view(), name="start-driving"),
    path(
        "trip/start-sleep-breth/", startSleepBreth.as_view(), name="start-sleep-breth"
    ),
    path("trip/start-off-duty/", StartOffDuty.as_view(), name="start-off-duty"),
    path("trip/start-on-duty/", StartOnDuty.as_view(), name="start-on-duty"),
    path("trip/log-off-duty/", LogOffDuty.as_view(), name="log-off-duty"),
    path("logs/", LogView.as_view(), name="log-list"),
]
