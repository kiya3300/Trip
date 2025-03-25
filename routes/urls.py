from django.urls import path
from .views import RouteListView  # Ensure you have at least one view

urlpatterns = [
    path('', RouteListView.as_view(), name='route-list'),
]
