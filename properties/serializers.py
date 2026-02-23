from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True, source='owner')
    
    class Meta:
        model = Property
        fields = [
            'id', 'name', 'property_type', 'description',
            'address', 'city', 'state', 'zip_code', 'country',
            'bedrooms', 'bathrooms', 'square_footage',
            'rent_amount', 'security_deposit', 'status',
            'owner', 'owner_id',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']


class PropertyListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list views"""
    owner = serializers.StringRelatedField()
    
    class Meta:
        model = Property
        fields = [
            'id', 'name', 'property_type', 'city',
            'bedrooms', 'bathrooms', 'rent_amount', 'status',
            'owner', 'created_at'
        ]