from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    tenant_username = serializers.CharField(source='tenant.username', read_only=True)
    apartment_title = serializers.CharField(source='apartment.title', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'apartment', 'tenant', 'tenant_username', 'apartment_title', 'check_in_date', 'check_out_date', 'timestamp']
        read_only_fields = ['tenant', 'timestamp']