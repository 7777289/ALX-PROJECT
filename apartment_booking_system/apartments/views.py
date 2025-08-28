from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Apartment
from .serializers import ApartmentSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class ApartmentListCreateView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ApartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]
    
class MyApartmentListView(generics.ListAPIView):
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter apartments to show only the ones owned by the current user
        return Apartment.objects.filter(owner=self.request.user)