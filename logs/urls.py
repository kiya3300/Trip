from django.urls import path
from .views import LogListView  # Ensure you have a view like LogListView
urlpatterns = [
    path('', LogListView.as_view(), name='log-list'),
]