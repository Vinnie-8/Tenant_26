from rest_framework import serializers
from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    """Serializer for Tenant CRUD operations"""
    
    class Meta:
        model = Tenant
        fields = [
            'id', 'name', 'domain', 'owner_email',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_domain(self, value):
        """Validate and normalize domain"""
        value = value.lower().strip()
        
        # Check if domain already exists
        if self.instance:
            if Tenant.objects.filter(domain=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("This domain is already in use.")
        else:
            if Tenant.objects.filter(domain=value).exists():
                raise serializers.ValidationError("This domain is already in use.")
        
        return value
    
    def validate_owner_email(self, value):
        """Validate email format"""
        if value:
            value = value.lower().strip()
        return value


class TenantListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list views"""
    
    class Meta:
        model = Tenant
        fields = ['id', 'name', 'domain', 'is_active', 'created_at']


class TenantSimpleSerializer(serializers.ModelSerializer):
    """Minimal serializer for nested representations"""
    
    class Meta:
        model = Tenant
        fields = ['id', 'name', 'domain']