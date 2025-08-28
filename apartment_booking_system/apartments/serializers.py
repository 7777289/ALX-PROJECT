from rest_framework import serializers
from .models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Apartment
        fields = ['id', 'title', 'description', 'location', 'price', 'size', 'availability', 'owner', 'owner_username']
        read_only_fields = ['owner']