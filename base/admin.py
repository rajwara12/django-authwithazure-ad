from django.contrib import admin
from django.contrib.auth.models import Group
# Eliminate Group from Admin Portal
admin.site.unregister(Group)
# Customization of Django Portal
admin.site.site_header = "Django-Azure AD Admin Panel"
admin.site.site_title = "Django-Azure AD Admin Portal"
admin.site.index_title = "Welcome to Django-Azure AD Portal"