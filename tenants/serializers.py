from rest_framework import serializers
from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'name', 'domain', 'owner_email', 'created_at']
        read_only_fields = ['id', 'created_at']
