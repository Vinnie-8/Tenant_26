from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200, unique=True)
    owner_email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.domain})"
