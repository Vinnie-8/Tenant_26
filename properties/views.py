from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Property
from .serializers import PropertySerializer, PropertyListSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Only owners can edit their properties"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # ✅ Fixed
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'city', 'description']
    ordering_fields = ['created_at', 'rent_amount', 'name']
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Property.objects.filter(
                Q(owner=user) | Q(status='available')
            ).distinct()
        return Property.objects.filter(status='available')

    def get_serializer_class(self):
        if self.action == 'list':
            return PropertyListSerializer
        return PropertySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])  # ✅ Protect this
    def my_properties(self, request):
        properties = Property.objects.filter(owner=request.user)
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])  # ✅ Protect this
    def mark_available(self, request, pk=None):
        property = self.get_object()
        property.status = 'available'
        property.save()
        return Response({'status': 'Property marked as available'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])  # ✅ Protect this
    def mark_occupied(self, request, pk=None):
        property = self.get_object()
        property.status = 'occupied'
        property.save()
        return Response({'status': 'Property marked as occupied'})
