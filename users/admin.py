from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'provider')
