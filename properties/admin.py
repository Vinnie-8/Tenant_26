from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'property_type', 'city', 'state',
        'rent_amount', 'status', 'owner', 'created_at'
    ]
    list_filter = [
        'property_type', 'status', 'city', 'state',
        'bedrooms', 'bathrooms', 'created_at'
    ]
    search_fields = ['name', 'address', 'city', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    # Ordering
    ordering = ['-created_at']
    
    # List per page
    list_per_page = 25
    
    # Fieldsets for organized form view
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'property_type', 'description', 'owner')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code', 'country')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'square_footage')
        }),
        ('Pricing', {
            'fields': ('rent_amount', 'security_deposit')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Filter horizontally for many-to-many (if you add amenities later)
    # filter_horizontal = ['amenities']
    
    # Date hierarchy for easy navigation
    date_hierarchy = 'created_at'
    
    # Custom actions
    actions = ['mark_as_available', 'mark_as_occupied', 'mark_as_maintenance']
    
    @admin.action(description='Mark selected properties as Available')
    def mark_as_available(self, request, queryset):
        queryset.update(status='available')
        
    @admin.action(description='Mark selected properties as Occupied')
    def mark_as_occupied(self, request, queryset):
        queryset.update(status='occupied')
        
    @admin.action(description='Mark selected properties as Under Maintenance')
    def mark_as_maintenance(self, request, queryset):
        queryset.update(status='maintenance')