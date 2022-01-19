from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'phonenum')
    list_filter = ('email', 'username', 'is_active', 'is_staff', 'phone_num')
    list_display = ('email', 'username',
                    'is_active', 'is_staff', 'phone_num')
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
