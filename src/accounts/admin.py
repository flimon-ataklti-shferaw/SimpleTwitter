from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

from .models import UserProfile

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm #update view
    add_form = UserAdminCreationForm #create view

    list_display = ['email', 'active', 'staff', 'admin']
    list_filter = ['admin', 'staff', 'active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2')}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.register(UserProfile)

admin.site.unregister(Group)

