from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/apartments/', include('apartments.urls')),
    path('api/bookings/', include('bookings.urls')),
]
