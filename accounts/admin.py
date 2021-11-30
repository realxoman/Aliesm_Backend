from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from .models import *
from django.contrib.auth.models import Group



# ----------------------------- Unregister Group ---------------------------
admin.site.unregister(Group)


# ----------------------------- User ---------------------------------------
@register(User)
class UserAdmin(AbstractUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone',
                    'get_date_joined', 'get_last_update', 'is_active', 'is_superuser', 'is_manager']

    list_filter = ['is_active', 'is_superuser', 'is_manager']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    readonly_fields = ['get_date_joined',
                       'get_last_update', 'get_last_login']
    list_display_links = ['username']

    fieldsets = (
        ('Login Details', {
            'fields': ('username', 'password')
        }),

        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'is_manager',
                'user_permissions',
            )
        }),

        ('Important dates', {'fields': ('get_date_joined',
                                      'get_last_update', 'get_last_login')})
    )

    add_fieldsets = (
        ('Login Details', {
            'fields': ('username', 'password1', 'password2')
        }),

        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'is_manager',
                'user_permissions',
            )
        })
    )
