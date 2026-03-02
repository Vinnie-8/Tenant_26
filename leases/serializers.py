from rest_framework import serializers
from .models import Lease


class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = [
            'id', 'property_ref', 'tenant', 'start_date', 'end_date',
            'monthly_rent', 'security_deposit', 'status', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        if data.get('start_date') and data.get('end_date'):
            if data['start_date'] >= data['end_date']:
                raise serializers.ValidationError(
                    "Start date must be before end date."
                )
        return data


class LeaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = [
            'id', 'property_ref', 'tenant', 'start_date', 'end_date',
            'monthly_rent', 'status', 'created_at'
        ]