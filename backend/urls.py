from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/trips/', include('trips.urls')),  # Ensure this is set correctly
    path('api/routes/', include('routes.urls')),  # Assuming you have a routes app
    path('api/logs/', include('logs.urls')),  # Assuming you have a logs app
    # JWT Token Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
