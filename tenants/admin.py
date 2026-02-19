from django.contrib import admin
from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'owner_email', 'created_at')
    search_fields = ('name', 'domain', 'owner_email')
