from django.db import models


class Tenant(models.Model):
    """
    Multi-tenant model using same database with tenant_id separation.
    """
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200, unique=True)
    owner_email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return f"{self.name} ({self.domain})"