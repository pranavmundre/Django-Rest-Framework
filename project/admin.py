from django.contrib import admin

from project.models import Project, Board, Card


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_date', 'created_date')
    # readonly_fields = ('password', 'last_login', 'updated_date', 'date_joined')
    list_filter = ('created_date', )


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # readonly_fields = ('password', 'last_login', 'updated_date', 'date_joined')


class CardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # readonly_fields = ('password', 'last_login', 'updated_date', 'date_joined')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Card, ProjectAdmin)
