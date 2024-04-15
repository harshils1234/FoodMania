"""This file is used to display models in the Django admin panel."""

from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from user.models import User, UserAddress

admin.site.unregister(Group)
admin.site.site_header = "Foodmania"


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    This class will register user model in admin site.
    """
    date_hierarchy = 'date_joined'
    search_fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']
    list_display = ['username', 'email', 'phone_number', 'profile_image']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    list_per_page = 10

    def profile_image(self, obj):
        return format_html("<img src='{}' width='55' height='55'/>".format(obj.image.url))

    profile_image.short_description = 'Profile Image'


@admin.register(UserAddress)
class UserAddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    This class will register user address in admin site.
    """
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email',
                     'user__phone_number']
    list_display = ['user', 'type']
    list_per_page = 10
