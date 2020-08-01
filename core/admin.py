from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ["name",'email']
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        (_('Personal Info'), {'fields':('name',)}),
        (_('Permission'),{'fields': ("is_active", "is_superuser","is_staff")}),
        (_('Important Date'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes':('wide,'),
            'fields':('email','password1','password2')
        }),
         
    )
admin.site.register(models.User, UserAdmin)