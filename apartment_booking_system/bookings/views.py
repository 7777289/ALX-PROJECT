from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from users.models import User
from apartments.models import Apartment

class IsTenantOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action == 'create' and request.user.role == 'tenant':
                return True
            if view.action == 'list' and request.user.role == 'owner':
                return True
        return False

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'tenant':
            return Booking.objects.filter(tenant=user).select_related('apartment')
        elif user.role == 'owner':
            return Booking.objects.filter(apartment__owner=user).select_related('apartment', 'tenant')
        return Booking.objects.none()

    def create(self, request, *args, **kwargs):
        if request.user.role != 'tenant':
            return Response({"detail": "Only tenants can create bookings."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(tenant=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)