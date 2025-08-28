from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/apartments/', include('apartments.urls')),
    path('api/bookings/', include('bookings.urls')),
    
    # Add this line to redirect the root URL to a different path
    path('', RedirectView.as_view(url='admin/')),
]