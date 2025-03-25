from trips.models import DrivringTrip, OffDuty, OnDuty, SleepBerth
from django.utils.timezone import now


def end_active_status(user, log):
    if DrivringTrip.objects.filter(
        user=user, log_data=log, created_at__gte=log.started_at
    ).exists():
        active_status = DrivringTrip.objects.filter(user=user, log_data=log).last()
    elif OffDuty.objects.filter(
        user=user, log_data=log, ended_at__isnull=True
    ).exists():
        active_status = OffDuty.objects.filter(
            user=user, log_data=log, ended_at__isnull=True
        ).last()
    elif SleepBerth.objects.filter(
        user=user, log_data=log, ended_at__isnull=True
    ).exists():
        active_status = SleepBerth.objects.filter(
            user=user, log_data=log, ended_at__isnull=True
        ).last()
    elif OnDuty.objects.filter(user=user, log_data=log, ended_at__isnull=True).exists():
        active_status = OnDuty.objects.filter(
            user=user, log_data=log, ended_at__isnull=True
        ).last()

    # Step 3: End the current status
    if active_status:
        active_status.ended_at = now()
        active_status.save()
