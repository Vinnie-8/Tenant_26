from django.contrib import admin
from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'domain', 'owner_email', 'is_active', 'created_at'
    ]
    list_filter = [
        'is_active', 'created_at'
    ]
    search_fields = [
        'name', 'domain', 'owner_email'
    ]
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    # Ordering
    ordering = ['-created_at']
    
    # List per page
    list_per_page = 25
    
    # Fieldsets for organized form view
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'domain', 'owner_email', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Custom actions
    actions = ['activate_tenant', 'deactivate_tenant']
    
    @admin.action(description='Activate selected tenants')
    def activate_tenant(self, request, queryset):
        queryset.update(is_active=True)
    
    @admin.action(description='Deactivate selected tenants')
    def deactivate_tenant(self, request, queryset):
        queryset.update(is_active=False)