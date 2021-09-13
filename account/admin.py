from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    readonly_fields = ('password', 'last_login', 'updated_date', 'date_joined')
    # list_filter = ('date_joined',)


admin.site.register(User, UserAdmin)
