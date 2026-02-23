from django.contrib import admin
from django.contrib.auth.models import User, Group

# You can also customize the admin site header
admin.site.site_header = 'Tenant Management System'
admin.site.site_title = 'Tenant Admin'
admin.site.index_title = 'Property Management'

# Optional: Group users by app
admin.site.unregister(Group)