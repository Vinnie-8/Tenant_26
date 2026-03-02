from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tenant
from .serializers import (
    TenantSerializer,
    TenantListSerializer,
    TenantSimpleSerializer
)


class TenantViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tenants.
    
    Endpoints:
    - GET /api/tenants/ - List all tenants
    - POST /api/tenants/ - Create new tenant
    - GET /api/tenants/{id}/ - Get tenant details
    - PUT /api/tenants/{id}/ - Update tenant
    - DELETE /api/tenants/{id}/ - Delete tenant
    """
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter tenants based on user permissions"""
        user = self.request.user
        
        # Superusers can see all tenants
        if user.is_superuser:
            return Tenant.objects.all()
        
        # Regular users can only see their own tenant
        if hasattr(user, 'tenant') and user.tenant:
            return Tenant.objects.filter(id=user.tenant.id)
        
        return Tenant.objects.none()
    
    def get_serializer_class(self):
        """Return different serializers for different actions"""
        if self.action == 'list':
            return TenantListSerializer
        return TenantSerializer
    
    def perform_create(self, serializer):
        """Create tenant and associate with user"""
        tenant = serializer.save()
        
        # Associate user with this tenant
        self.request.user.tenant = tenant
        self.request.user.save()
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active tenants"""
        tenants = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(tenants, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def my_tenant(self, request):
        """Get the current user's tenant"""
        if hasattr(request.user, 'tenant') and request.user.tenant:
            serializer = self.get_serializer(request.user.tenant)
            return Response(serializer.data)
        return Response(
            {'error': 'User is not associated with any tenant'},
            status=status.HTTP_404_NOT_FOUND
        )