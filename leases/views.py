from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date
from django.db.models import Q
from .models import Lease
from .serializers import LeaseSerializer, LeaseListSerializer


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Lease.objects.all()
        if hasattr(user, 'tenant') and user.tenant:
            return Lease.objects.filter(tenant=user.tenant)
        return Lease.objects.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return LeaseListSerializer
        return LeaseSerializer

    @action(detail=False, methods=['get'])
    def active(self, request):
        leases = self.get_queryset().filter(status='active')
        serializer = self.get_serializer(leases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def expired(self, request):
        leases = self.get_queryset().filter(status='expired')
        serializer = self.get_serializer(leases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        leases = self.get_queryset().filter(status='pending')
        serializer = self.get_serializer(leases, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        lease = self.get_object()
        lease.status = 'active'
        lease.save()
        return Response({'status': 'Lease activated'})

    @action(detail=True, methods=['post'])
    def expire(self, request, pk=None):
        lease = self.get_object()
        lease.status = 'expired'
        lease.save()
        return Response({'status': 'Lease expired'})

    @action(detail=True, methods=['post'])
    def terminate(self, request, pk=None):
        lease = self.get_object()
        lease.status = 'terminated'
        lease.save()
        return Response({'status': 'Lease terminated'})