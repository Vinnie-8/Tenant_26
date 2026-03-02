from django.contrib import admin
from django.utils.html import format_html
from .models import Lease


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'property_link', 'tenant_link', 'start_date', 'end_date',
        'monthly_rent', 'status', 'created_at'
    ]
    list_filter = [
        'status', 'start_date', 'end_date', 'created_at'
    ]
    search_fields = [
        'property_ref__name', 'tenant__name', 'notes'
    ]
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    ordering = ['-created_at']
    list_per_page = 25
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Property & Tenant', {
            'fields': ('property_ref', 'tenant')
        }),
        ('Lease Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Pricing', {
            'fields': ('monthly_rent', 'security_deposit')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['activate_leases', 'expire_leases', 'terminate_leases']

    def property_link(self, obj):
        return format_html(
            '<a href="/admin/properties/property/{}/change/">{}</a>',
            obj.property_ref.id, obj.property_ref.name
        )
    property_link.short_description = 'Property'

    def tenant_link(self, obj):
        return format_html(
            '<a href="/admin/tenants/tenant/{}/change/">{}</a>',
            obj.tenant.id, obj.tenant.name
        )
    tenant_link.short_description = 'Tenant'

    @admin.action(description='Activate selected leases')
    def activate_leases(self, request, queryset):
        queryset.update(status='active')

    @admin.action(description='Mark selected leases as expired')
    def expire_leases(self, request, queryset):
        queryset.update(status='expired')

    @admin.action(description='Terminate selected leases')
    def terminate_leases(self, request, queryset):
        queryset.update(status='terminated')